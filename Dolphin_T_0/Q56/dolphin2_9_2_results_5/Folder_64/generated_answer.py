def all_substring_of_size_n(string):
    if len(string) < 8:
        return []
    substrings = set()
    for i in range(len(string) - 7):
        substring = string[i:i + 8]
        if len(set(list(substring))) == 8:
            substrings.add(substring)
    return list(substrings)