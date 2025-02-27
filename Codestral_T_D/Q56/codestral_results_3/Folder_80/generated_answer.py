def all_substring_of_size_n(s):
    substrings = []
    length = len(s)
    for i in range(length - 30):
        substring = s[i:i + 31]
        if len(set(substring)) == 31:
            substrings.append(substring)
    return substrings