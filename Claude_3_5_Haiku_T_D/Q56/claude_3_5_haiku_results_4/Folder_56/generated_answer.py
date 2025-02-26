def all_substring_of_size_n(string):
    n = 69
    distinct_substrings = set()
    if len(string) < n:
        return list(distinct_substrings)
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(set(substring)) == n:
            distinct_substrings.add(substring)
    return list(distinct_substrings)