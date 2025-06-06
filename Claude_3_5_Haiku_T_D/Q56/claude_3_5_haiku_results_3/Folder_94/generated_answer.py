def all_substring_of_size_n(s):
    distinct_substrings = set()
    n = 70
    if len(s) < n:
        return []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            distinct_substrings.add(substring)
    return list(distinct_substrings)