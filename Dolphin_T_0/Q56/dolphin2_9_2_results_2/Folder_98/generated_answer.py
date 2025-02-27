def all_substring_of_size_n(s):
    substrings = []
    n = 10
    for i in range(len(s) - n + 1):
        subs = s[i:i + n]
        if len(set(subs)) == n and subs not in substrings:
            substrings.append(subs)
    return substrings