def all_substring_of_size_n(string):
    if len(string) < 70:
        return []
    substrings = set()
    for i in range(len(string) - 69):
        if len(set(string[i:i + 70])) == 70:
            substrings.add(string[i:i + 70])
    return list(substrings)