def all_substring_of_size_n(string):
    n = 46
    substrings = []
    for i in range(len(string)):
        for j in range(i + n, len(string) + 1):
            sub = string[i:j]
            if len(set(sub)) == n:
                substrings.append(sub)
    return substrings