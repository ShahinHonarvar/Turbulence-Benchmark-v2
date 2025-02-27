def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 18):
        sub = string[i:i + 19]
        if len(set(sub)) == 19:
            substrings.append(sub)
    return substrings