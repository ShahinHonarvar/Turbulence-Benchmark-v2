def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 73):
        substring = string[i:i + 74]
        if len(set(substring)) == 74:
            substrings.append(substring)
    return substrings