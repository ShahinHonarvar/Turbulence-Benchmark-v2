def all_substring_of_size_n(s):
    n = 60
    distinct_substrings = []
    if len(s) < n:
        return distinct_substrings
    for i in range(len(s) - n + 1):
        if len(set(s[i:i + n])) == n:
            distinct_substrings.append(s[i:i + n])
    return list(set(distinct_substrings))