def all_substring_of_size_n(s):
    if len(s) < 65:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 64):
        substring = s[i:i + 65]
        if len(set(substring)) == 65:
            distinct_substrings.add(substring)
    return list(distinct_substrings)