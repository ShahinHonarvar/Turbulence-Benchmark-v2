def all_substring_of_size_n(str):
    if len(str) < 44:
        return []
    substrings = set()
    for i in range(len(str) - 43):
        substring = str[i:i + 44]
        if len(set(substring)) == 44:
            substrings.add(substring)
    return list(substrings)