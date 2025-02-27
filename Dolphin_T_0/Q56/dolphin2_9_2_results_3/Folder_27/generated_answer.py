def all_substring_of_size_n(string):
    if not isinstance(string, str):
        return []
    if len(set(string)) < 57:
        return []
    substrings = set()
    for i in range(len(string) - 56):
        substring = string[i:i + 57]
        if len(set(substring)) == 57:
            substrings.add(substring)
    return list(substrings)