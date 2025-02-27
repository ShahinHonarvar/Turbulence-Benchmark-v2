def all_substring_of_size_n(string):
    n = 65
    substrings = set()
    for i in range(len(string) - n + 1):
        sub = string[i:i + n]
        if len(set(sub)) == n:
            substrings.add(sub)
    return list(substrings)