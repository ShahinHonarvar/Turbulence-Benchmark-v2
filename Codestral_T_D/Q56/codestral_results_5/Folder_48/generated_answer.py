def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 120 + 1):
        substring = string[i:i + 120]
        if len(set(substring)) == 120:
            substrings.add(substring)
    return list(substrings)