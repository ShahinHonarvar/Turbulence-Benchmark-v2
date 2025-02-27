def all_substring_of_size_n(string):
    if len(string) < 32:
        return []
    substrings = set()
    for i in range(len(string) - 31):
        sub = string[i:i + 32]
        if len(set(sub)) == 32:
            substrings.add(sub)
    return list(substrings)