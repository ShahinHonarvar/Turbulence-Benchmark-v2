def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 63 + 1):
        substring = string[i:i + 63]
        if len(set(substring)) == 63:
            substrings.add(substring)
    return list(substrings)