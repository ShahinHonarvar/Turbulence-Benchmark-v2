def all_substring_of_size_n(s):
    n = 63
    distinct_substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            distinct_substrings.append(substring)
    return list(set(distinct_substrings))