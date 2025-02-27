def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 143 + 1):
        substring = s[i:i + 143]
        if len(set(substring)) == 143:
            if substring not in substrings:
                substrings.append(substring)
    return substrings