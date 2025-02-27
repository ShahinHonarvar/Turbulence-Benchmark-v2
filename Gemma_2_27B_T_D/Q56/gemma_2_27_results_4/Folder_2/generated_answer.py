def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 55):
        substring = string[i:i + 56]
        if len(set(substring)) == 56:
            substrings.add(substring)
    return list(substrings)