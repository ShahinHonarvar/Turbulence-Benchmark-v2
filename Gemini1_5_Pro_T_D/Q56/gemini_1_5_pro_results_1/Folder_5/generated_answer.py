def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 64:
        return substrings
    for i in range(len(s) - 63):
        substring = s[i:i + 64]
        if len(set(substring)) == 64 and substring not in substrings:
            substrings.append(substring)
    return substrings