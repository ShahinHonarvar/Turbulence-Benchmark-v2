def all_substring_of_size_n(s):
    if len(s) < 48:
        return []
    unique_substrings = set()
    for i in range(len(s) - 47):
        substring = s[i:i + 48]
        if len(set(substring)) == 48:
            unique_substrings.add(substring)
    return list(unique_substrings)