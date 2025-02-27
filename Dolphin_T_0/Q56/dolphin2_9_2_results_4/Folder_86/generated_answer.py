def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 142):
        sub = string[i:i + 143]
        if len(set(sub)) == len(sub):
            substrings.add(sub)
    return list(substrings)