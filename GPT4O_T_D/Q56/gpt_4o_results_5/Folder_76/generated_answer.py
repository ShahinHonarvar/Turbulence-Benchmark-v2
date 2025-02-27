def all_substring_of_size_n(s):

    def has_unique_characters(substr):
        return len(substr) == len(set(substr))
    n = 149
    substrings = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if has_unique_characters(substring):
            substrings.add(substring)
    return list(substrings)