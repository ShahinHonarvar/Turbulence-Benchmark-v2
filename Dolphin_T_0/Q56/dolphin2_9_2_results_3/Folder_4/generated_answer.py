def all_substring_of_size_n(string):
    if len(string) < 41:
        return []
    substrings = set()
    for i in range(len(string) - 40):
        substring = string[i:i + 41]
        if len(set(substring)) == 41:
            substrings.add(substring)
    return list(substrings)