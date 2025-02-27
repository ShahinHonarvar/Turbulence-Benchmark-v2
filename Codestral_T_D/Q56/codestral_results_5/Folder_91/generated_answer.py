def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 5):
        sub = string[i:i + 6]
        if len(set(sub)) == 6:
            substrings.append(sub)
    return substrings