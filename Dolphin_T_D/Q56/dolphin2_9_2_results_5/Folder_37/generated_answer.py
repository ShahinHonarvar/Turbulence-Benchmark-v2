def all_substring_of_size_n(string):
    if len(string) < 65:
        return []
    unique_substrings = set()
    for i in range(len(string) - 5):
        substring = string[i:i + 65]
        if len(set(substring)) == 65:
            unique_substrings.add(substring)
    return list(unique_substrings)