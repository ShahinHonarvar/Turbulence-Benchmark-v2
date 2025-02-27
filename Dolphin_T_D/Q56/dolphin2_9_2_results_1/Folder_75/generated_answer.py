def all_substring_of_size_n(string):
    substrings = set()
    n = 16
    for i in range(len(string) - n + 1):
        sub = string[i:i + n]
        if len(set(sub)) == n:
            substrings.add(sub)
    return list(substrings)