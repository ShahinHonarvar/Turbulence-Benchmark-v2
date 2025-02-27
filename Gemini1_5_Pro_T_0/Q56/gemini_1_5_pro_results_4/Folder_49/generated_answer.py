def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 73:
        return substrings
    for i in range(len(s) - 72):
        substring = s[i:i + 73]
        if len(set(substring)) == 73:
            if substring not in substrings:
                substrings.append(substring)
    return substrings