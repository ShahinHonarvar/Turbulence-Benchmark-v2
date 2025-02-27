def all_substring_of_size_n(string):
    if len(string) < 21:
        return []
    substrings = set()
    for i in range(len(string) - 20):
        sub = string[i:i + 21]
        if len(set(sub)) == 21:
            substrings.add(sub)
    if len(substrings) > 0:
        return list(substrings)
    else:
        return []