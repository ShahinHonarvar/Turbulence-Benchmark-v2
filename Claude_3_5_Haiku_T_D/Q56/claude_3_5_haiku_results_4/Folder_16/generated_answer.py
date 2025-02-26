def all_substring_of_size_n(string):
    if len(string) < 124:
        return []
    unique_substrings = set()
    for i in range(len(string) - 123):
        substring = string[i:i + 124]
        if len(set(substring)) == 124:
            unique_substrings.add(substring)
    return list(unique_substrings)