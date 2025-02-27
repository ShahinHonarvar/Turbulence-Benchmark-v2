def all_substring_of_size_n(string):
    if len(string) < 70:
        return []
    substrings = set()
    for i in range(len(string) - 69):
        sub = string[i:i + 70]
        if len(set(sub)) == len(sub):
            substrings.add(sub)
    return list(substrings)