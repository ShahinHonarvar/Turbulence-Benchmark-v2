def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 88, len(s) + 1):
            substring = s[i:j]
            if len(set(substring)) == 88:
                substrings.append(substring)
    return substrings