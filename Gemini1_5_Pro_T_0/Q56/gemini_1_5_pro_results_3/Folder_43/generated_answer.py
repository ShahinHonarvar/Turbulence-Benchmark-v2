def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 86:
        return substrings
    for i in range(0, len(s) - 85):
        substring = s[i:i + 86]
        if len(set(substring)) == 86 and substring not in substrings:
            substrings.append(substring)
    return substrings