def all_substring_of_size_n(s):

    def has_unique_chars(substring):
        return len(set(substring)) == len(substring)
    substrings = []
    n = 40
    if len(s) < n:
        return substrings
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if has_unique_chars(substring):
            substrings.append(substring)
    return list(set(substrings))