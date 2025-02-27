def all_substring_of_size_n(s):
    n = 7
    substrings = []
    for i in range(len(s) - n + 1):
        subs = s[i:i + n]
        if len(set(subs)) == n:
            substrings.append(subs)
    return substrings