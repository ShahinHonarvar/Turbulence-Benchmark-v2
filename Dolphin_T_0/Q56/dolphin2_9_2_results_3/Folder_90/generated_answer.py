def all_substring_of_size_n(string):
    n = 130
    substrings = []
    for i in range(len(string)):
        if len(string[i:i + n]) == n:
            if len(set(string[i:i + n])) == n:
                substrings.append(string[i:i + n])
    return substrings