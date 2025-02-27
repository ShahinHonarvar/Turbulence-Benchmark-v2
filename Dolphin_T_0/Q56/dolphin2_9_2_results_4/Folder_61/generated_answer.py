def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 38):
        sub = string[i:i + 39]
        if len(set(sub)) == 39:
            substrings.append(sub)
    return substrings