def all_substring_of_size_n(string):
    if len(string) < 2:
        return []
    substrings = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            substring = string[i:j + 1]
            if len(substring) == 2 and len(set(substring)) == 2:
                substrings.add(substring)
    return list(substrings)