def all_substring_of_size_n(s):
    n = 46
    if len(s) < n:
        return []
    else:
        substrings = []
        for i in range(len(s) - n + 1):
            if len(set(s[i:i + n])) == n and s[i:i + n] not in substrings:
                substrings.append(s[i:i + n])
        return substrings