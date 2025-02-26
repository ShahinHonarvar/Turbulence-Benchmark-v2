def all_substring_of_size_n(s):
    if len(s) < 55:
        return []
    unique_substrings = set()
    for i in range(len(s) - 54):
        substring = s[i:i + 55]
        if len(set(substring)) == 55:
            unique_substrings.add(substring)
    return list(unique_substrings)