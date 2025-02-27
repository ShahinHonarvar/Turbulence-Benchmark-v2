def all_substring_of_size_n(s):
    substrings = []
    if len(s) >= 43:
        for i in range(len(s) - 42):
            substring = s[i:i + 43]
            if len(set(substring)) == 43 and substring not in substrings:
                substrings.append(substring)
    return substrings