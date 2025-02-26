def all_substring_of_size_n(s):
    if len(s) < 97:
        return []
    unique_substrings = set()
    for i in range(len(s) - 96):
        substring = s[i:i + 97]
        if len(set(substring)) == 97:
            unique_substrings.add(substring)
    return list(unique_substrings)