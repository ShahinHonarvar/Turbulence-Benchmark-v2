def all_substring_of_size_n(string):
    length = 117
    if len(string) < length:
        return []
    substrings = {}
    for i in range(len(string) - length + 1):
        sub = string[i:i + length]
        if len(set(sub)) == length:
            substrings[sub] = True
    return list(substrings.keys())