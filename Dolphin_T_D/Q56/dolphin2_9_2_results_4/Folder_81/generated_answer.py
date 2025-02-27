def all_substring_of_size_n(s):
    length = len(s)
    substrings = []
    for i in range(length - 97):
        sub = s[i:i + 98]
        if len(set(sub)) == 98:
            substrings.append(sub)
    return list(set(substrings))