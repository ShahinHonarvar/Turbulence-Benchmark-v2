def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 47):
        substring = string[i:i + 48]
        if len(set(substring)) == 48:
            substrings.add(substring)
    return list(substrings)