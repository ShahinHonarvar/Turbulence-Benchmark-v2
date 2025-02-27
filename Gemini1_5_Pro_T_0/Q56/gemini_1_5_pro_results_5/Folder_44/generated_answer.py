def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 90:
        return substrings
    for i in range(len(s) - 89):
        substring = s[i:i + 90]
        if len(set(substring)) == 90:
            substrings.append(substring)
    return substrings