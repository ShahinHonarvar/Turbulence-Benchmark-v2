def all_substring_of_size_n(string):
    n = 63
    substrings = set()
    for i in range(len(string)):
        for j in range(i + n, len(string) + 1):
            sub = string[i:j]
            if len(sub) == n and len(set(sub)) == n:
                substrings.add(sub)
    return list(substrings)