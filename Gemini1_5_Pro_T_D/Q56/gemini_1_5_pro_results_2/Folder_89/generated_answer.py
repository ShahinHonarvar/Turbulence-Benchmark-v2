def all_substring_of_size_n(s):
    substrings = []
    if len(s) >= 38:
        for i in range(len(s) - 37):
            substring = s[i:i + 38]
            if len(set(substring)) == 38 and substring not in substrings:
                substrings.append(substring)
    return substrings