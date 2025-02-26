def all_substring_of_size_n(s):
    if len(s) < 39:
        return []
    distinct_substrings = set()
    for i in range(len(s) - 38):
        substring = s[i:i + 39]
        if len(set(substring)) == 39:
            distinct_substrings.add(substring)
    return list(distinct_substrings)