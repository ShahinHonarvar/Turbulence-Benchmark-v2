def all_substring_of_size_n(s):
    n = 24
    distinct_substrings = set()
    if len(s) < n:
        return list(distinct_substrings)
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            distinct_substrings.add(substring)
    return list(distinct_substrings)