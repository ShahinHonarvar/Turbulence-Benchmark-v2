def all_substring_of_size_n(s):
    substrings = []
    length = len(s)
    for i in range(length - 49):
        substring = s[i:i + 50]
        if len(set(substring)) == 50:
            substrings.append(substring)
    return substrings