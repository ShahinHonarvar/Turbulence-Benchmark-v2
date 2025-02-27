def all_substring_of_size_n(s):

    def has_unique_chars(substring):
        return len(set(substring)) == len(substring)
    n = 40
    result = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if has_unique_chars(substring):
            result.append(substring)
    return result