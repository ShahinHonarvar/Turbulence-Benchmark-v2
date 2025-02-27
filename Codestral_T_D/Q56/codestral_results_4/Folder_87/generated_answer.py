def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 58, len(s) + 1):
            sub = s[i:j]
            if len(sub) == len(set(sub)):
                substrings.append(sub)
    return substrings