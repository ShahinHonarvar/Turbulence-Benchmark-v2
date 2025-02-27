def all_substring_of_size_n(string):
    n = 50
    if len(string) < n:
        return []
    substrings = set()
    for i in range(len(string)):
        sub = string[i:i + n]
        if len(set(sub)) == n:
            substrings.add(sub)
    return list(substrings)