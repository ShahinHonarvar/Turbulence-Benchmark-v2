def all_substring_of_size_n(s):
    n = 22
    distinct_substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n and substring not in distinct_substrings:
            distinct_substrings.append(substring)
    return distinct_substrings