def all_substring_of_size_n(s):
    if len(s) < 41:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 40):
        substring = s[i:i + 41]
        if len(set(substring)) == 41:
            distinct_substrings.add(substring)
    return list(distinct_substrings)