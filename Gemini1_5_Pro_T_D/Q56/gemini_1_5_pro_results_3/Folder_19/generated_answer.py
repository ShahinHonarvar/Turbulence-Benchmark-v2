def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 17):
        substring = s[i:i + 18]
        if len(set(substring)) == 18:
            substrings.append(substring)
    return list(set(substrings))