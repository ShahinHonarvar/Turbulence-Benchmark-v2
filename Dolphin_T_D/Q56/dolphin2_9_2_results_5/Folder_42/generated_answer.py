def all_substring_of_size_n(s):
    n = 45
    substrings = []
    for i in range(len(s) - n + 1):
        curr = s[i:i + n]
        if len(curr) == len(set(curr)) and curr not in substrings:
            substrings.append(curr)
    return substrings