def all_substring_of_size_n(string):
    n = len(string)
    substrings = set()
    for i in range(n - 6):
        sub = string[i:i + 7]
        if len(set(sub)) == len(sub):
            substrings.add(sub)
    return list(substrings)