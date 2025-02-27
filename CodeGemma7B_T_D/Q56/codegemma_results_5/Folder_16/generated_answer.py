def all_substring_of_size_n(string):

    def is_unique(substring):
        unique_chars = set()
        for char in substring:
            if char in unique_chars:
                return False
            unique_chars.add(char)
        return True
    result = []
    for i in range(len(string) - 123):
        substring = string[i:i + 124]
        if is_unique(substring):
            result.append(substring)
    return result