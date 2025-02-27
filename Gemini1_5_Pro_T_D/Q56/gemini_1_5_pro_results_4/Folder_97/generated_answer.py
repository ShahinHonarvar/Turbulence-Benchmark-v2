def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 142 + 1):
        substring = s[i:i + 142]
        if len(set(substring)) == 142:
            substrings.append(substring)
    return substrings