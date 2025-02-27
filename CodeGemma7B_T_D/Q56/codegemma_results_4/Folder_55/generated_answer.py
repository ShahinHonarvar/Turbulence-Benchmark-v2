def all_substring_of_size_n(string):
    if len(string) <= 39:
        return []
    unique_substrings = set()
    for i in range(len(string) - 39):
        substring = string[i:i + 40]
        if len(set(substring)) == 40:
            unique_substrings.add(substring)
    return list(unique_substrings)