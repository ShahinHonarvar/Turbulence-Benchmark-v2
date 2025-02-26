def all_substring_of_size_n(s):
    if len(s) < 30:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 29):
        substring = s[i:i + 30]
        if len(set(substring)) == 30:
            distinct_substrings.add(substring)
    return list(distinct_substrings)