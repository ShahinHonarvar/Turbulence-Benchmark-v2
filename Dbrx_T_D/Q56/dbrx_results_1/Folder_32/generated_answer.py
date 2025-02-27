def all_substring_of_size_n(string):
    n = 71
    if len(string) < n:
        return []
    substrings = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(substring) == n and len(set(substring)) == n:
            substrings.add(''.join(sorted(substring)))
    return list(substrings)