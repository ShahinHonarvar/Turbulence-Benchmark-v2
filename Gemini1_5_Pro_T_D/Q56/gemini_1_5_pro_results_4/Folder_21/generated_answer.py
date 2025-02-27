def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 106 + 1):
        substring = string[i:i + 106]
        if len(set(substring)) == 106:
            if substring not in substrings:
                substrings.append(substring)
    return substrings