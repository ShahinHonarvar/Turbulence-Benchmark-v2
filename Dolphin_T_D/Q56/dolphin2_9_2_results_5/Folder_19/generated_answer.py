def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 18 + 1):
        sub = string[i:i + 19]
        if len(set(sub)) == len(sub):
            substrings.append(sub)
    return substrings