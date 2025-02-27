def all_substring_of_size_n(string):
    if len(string) < 54:
        return []
    substrings = set()
    for i in range(len(string) - 54):
        substring = string[i:i + 54]
        if len(set(substring)) == 54:
            substrings.add(substring)
    return list(substrings)