def all_substring_of_size_n(string):
    substrings = []
    n = 12
    if len(string) < n:
        return substrings
    for i in range(len(string) - n + 1):
        sub = string[i:i + n]
        if len(set(sub)) == n:
            substrings.append(sub)
    return list(set(substrings))