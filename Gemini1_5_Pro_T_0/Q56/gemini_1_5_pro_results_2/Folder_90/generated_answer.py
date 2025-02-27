def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 130:
        return substrings
    for i in range(len(s) - 129):
        substring = s[i:i + 130]
        if len(set(substring)) == 130:
            if substring not in substrings:
                substrings.append(substring)
    return substrings