def all_substring_of_size_n(string):
    if len(string) < 39:
        return []
    substrings = set()
    for i in range(len(string) - 38):
        substring = string[i:i + 39]
        if len(set(substring)) == 39:
            substrings.add(substring)
    return list(substrings)