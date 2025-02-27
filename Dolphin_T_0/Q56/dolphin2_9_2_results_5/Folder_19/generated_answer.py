def all_substring_of_size_n(s):
    n = 18
    substrings = []
    for i in range(len(s) - n + 1):
        k = s[i:i + n]
        if len(k) == len(set(k)) == n:
            substrings.append(k)
    return substrings