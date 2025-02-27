def all_substring_of_size_n(string):
    if len(string) < 74:
        return []
    substrings = set()
    for i in range(len(string) - 73):
        substring = string[i:i + 74]
        if len(set(substring)) == 74:
            substrings.add(substring)
    return list(substrings)