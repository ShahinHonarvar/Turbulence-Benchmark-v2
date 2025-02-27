def all_substring_of_size_n(s):
    substrings = []
    if len(s) >= 27:
        for i in range(len(s) - 26):
            substring = s[i:i + 27]
            if len(set(substring)) == 27:
                substrings.append(substring)
    return substrings