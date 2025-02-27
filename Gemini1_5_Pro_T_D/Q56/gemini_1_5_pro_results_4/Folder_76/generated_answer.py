def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 148):
        substring = s[i:i + 149]
        if len(set(substring)) == 149 and substring not in substrings:
            substrings.append(substring)
    return substrings