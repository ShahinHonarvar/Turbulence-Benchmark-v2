def all_substring_of_size_n(string):
    length = 86
    substrings = set()
    if len(string) < length:
        return []
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if len(set(substring)) == length:
            substrings.add(substring)
    return list(substrings)