def all_substring_of_size_n(s):

    def is_unique(substring):
        seen_characters = set()
        for char in substring:
            if char in seen_characters:
                return False
            seen_characters.add(char)
        return True
    return [substring for substring in [s[i:i + 75] for i in range(len(s) - 74)] if is_unique(substring)]