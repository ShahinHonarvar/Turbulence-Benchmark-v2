def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 98:
        return substrings
    for i in range(len(s) - 97):
        substring = s[i:i + 98]
        if len(set(substring)) == 98 and substring not in substrings:
            substrings.append(substring)
    return substrings