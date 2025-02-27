def all_substring_of_size_n(s):
    if len(s) < 56:
        return []
    unique_substrings = set()
    for i in range(len(s) - 55):
        substring = s[i:i + 56]
        if len(set(substring)) == 56:
            unique_substrings.add(substring)
    return list(unique_substrings)