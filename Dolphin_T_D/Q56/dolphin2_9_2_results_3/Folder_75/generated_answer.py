def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 15):
        sub = string[i:i + 16]
        if len(set(sub)) == 16:
            substrings.append(sub)
    return substrings