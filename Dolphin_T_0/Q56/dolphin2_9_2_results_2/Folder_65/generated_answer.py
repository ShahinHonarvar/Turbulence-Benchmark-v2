def all_substring_of_size_n(s):
    substrings = []
    if len(set(s)) != len(s):
        return substrings
    for i in range(len(s) - 80):
        if len(set(s[i:i + 81])) == 81:
            substrings.append(s[i:i + 81])
    return substrings