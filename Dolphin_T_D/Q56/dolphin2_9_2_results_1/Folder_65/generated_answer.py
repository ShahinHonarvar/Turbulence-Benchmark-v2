def all_substring_of_size_n(s):
    length = len(s)
    substrings = []
    for i in range(length - 7):
        sub = s[i:i + 81]
        if len(sub) == len(set(sub)) and len(sub) == 81:
            substrings.append(sub)
    return substrings