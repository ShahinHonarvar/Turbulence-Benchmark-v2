def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string)):
        if len(string) - i < 57:
            break
        substring = string[i:i + 57]
        if len(set(substring)) == 57:
            substrings.add(substring)
    return list(substrings)