def all_substring_of_size_n(str):

    def is_valid(substring):
        if len(substring) != 143:
            return False
        seen = set()
        for char in substring:
            if char in seen:
                return False
            seen.add(char)
        return True
    substrings = []
    for i in range(len(str) - 143 + 1):
        substring = str[i:i + 143]
        if is_valid(substring):
            substrings.append(substring)
    return substrings