def all_substring_of_size_n(s):
    if len(s) < 120:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 119):
        substring = s[i:i + 120]
        if len(set(substring)) == 120:
            distinct_substrings.add(substring)
    return list(distinct_substrings)