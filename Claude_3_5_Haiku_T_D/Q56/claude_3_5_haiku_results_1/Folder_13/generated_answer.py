def all_substring_of_size_n(s):
    if len(s) < 53:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 52):
        substring = s[i:i + 53]
        if len(set(substring)) == 53:
            distinct_substrings.add(substring)
    return list(distinct_substrings)