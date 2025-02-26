def all_substring_of_size_n(s):
    if len(s) < 43:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 42):
        substring = s[i:i + 43]
        if len(set(substring)) == 43:
            distinct_substrings.add(substring)
    return list(distinct_substrings)