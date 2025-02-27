def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 81, len(s) + 1):
            sub = s[i:j]
            if len(set(sub)) == 81:
                substrings.append(sub)
    return substrings