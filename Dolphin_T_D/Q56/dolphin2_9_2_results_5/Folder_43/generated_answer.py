def all_substring_of_size_n(s):
    n = 86
    substrings = []
    for i in range(len(s) - n + 1):
        sub_s = s[i:i + n]
        if len(set(sub_s)) == n:
            substrings.append(sub_s)
    return substrings