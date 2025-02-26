def all_substring_of_size_n(s):
    if len(s) < 100:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 99):
        substring = s[i:i + 100]
        if len(set(substring)) == 100:
            distinct_substrings.add(substring)
    return list(distinct_substrings)