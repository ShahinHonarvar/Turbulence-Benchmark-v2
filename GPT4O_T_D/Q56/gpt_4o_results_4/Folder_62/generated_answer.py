def all_substring_of_size_n(s):

    def has_unique_characters(substring):
        return len(set(substring)) == len(substring)
    n = 32
    if len(s) < n:
        return []
    unique_substrings = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if has_unique_characters(substr):
            unique_substrings.add(substr)
    return list(unique_substrings)