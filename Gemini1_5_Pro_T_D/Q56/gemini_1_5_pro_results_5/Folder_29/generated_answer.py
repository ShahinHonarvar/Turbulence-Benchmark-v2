def all_substring_of_size_n(s):
    substrings = []
    n = 95
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            if substring not in substrings:
                substrings.append(substring)
    return substrings