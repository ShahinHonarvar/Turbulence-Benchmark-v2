def all_substring_of_size_n(s):
    if len(s) < 24:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 23):
        substring = s[i:i + 24]
        if len(set(substring)) == 24:
            distinct_substrings.add(substring)
    return list(distinct_substrings)