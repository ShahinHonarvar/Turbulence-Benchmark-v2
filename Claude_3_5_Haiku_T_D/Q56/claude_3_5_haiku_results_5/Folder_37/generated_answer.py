def all_substring_of_size_n(s):
    if len(s) < 65:
        return []
    unique_substrings = set()
    for i in range(len(s) - 64):
        substring = s[i:i + 65]
        if len(set(substring)) == 65:
            unique_substrings.add(substring)
    return list(unique_substrings)