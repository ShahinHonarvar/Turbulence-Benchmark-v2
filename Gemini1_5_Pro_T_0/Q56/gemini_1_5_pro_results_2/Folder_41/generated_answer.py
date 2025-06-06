def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 74:
        return substrings
    for i in range(len(s) - 73):
        substring = s[i:i + 74]
        if len(set(substring)) == 74 and substring not in substrings:
            substrings.append(substring)
    return substrings