def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 83):
        substring = ''.join(sorted(set(string[i:i + 84])))
        if len(substring) == 84:
            substrings.append(substring)
    return list(set(substrings))