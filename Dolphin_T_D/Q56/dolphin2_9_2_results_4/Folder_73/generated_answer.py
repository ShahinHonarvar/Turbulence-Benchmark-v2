def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 19):
        sub = string[i:i + 20]
        if len(set(sub)) == 20:
            substrings.append(sub)
    return substrings