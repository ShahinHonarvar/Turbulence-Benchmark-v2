def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 92 + 1):
        substring = string[i:i + 92]
        if len(set(substring)) == 92:
            substrings.add(substring)
    return list(substrings)