def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 49):
        substring = s[i:i + 50]
        if len(substring) == 50 and len(set(substring)) == 50:
            substrings.append(substring)
    return list(set(substrings))