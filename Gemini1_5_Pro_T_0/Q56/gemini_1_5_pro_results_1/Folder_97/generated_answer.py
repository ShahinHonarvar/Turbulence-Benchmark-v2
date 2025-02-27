def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 142:
        return substrings
    for i in range(len(s) - 141):
        substring = s[i:i + 142]
        if len(set(substring)) == 142 and substring not in substrings:
            substrings.append(substring)
    return substrings