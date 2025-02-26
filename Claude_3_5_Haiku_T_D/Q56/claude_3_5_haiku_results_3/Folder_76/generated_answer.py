def all_substring_of_size_n(string):
    n = 149
    if len(string) < n:
        return []
    unique_substrings = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(set(substring)) == n:
            unique_substrings.add(substring)
    return list(unique_substrings)