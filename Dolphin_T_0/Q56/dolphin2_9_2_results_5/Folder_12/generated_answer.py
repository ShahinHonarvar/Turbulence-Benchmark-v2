def all_substring_of_size_n(s):
    length = 47
    substrings = []
    for i in range(0, len(s) - length + 1):
        sub = s[i:i + length]
        if len(set(sub)) == length:
            substrings.append(sub)
    return substrings