def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string)):
        if len(set(string[i:i + 35])) == 35:
            substrings.add(string[i:i + 35])
    return list(substrings)