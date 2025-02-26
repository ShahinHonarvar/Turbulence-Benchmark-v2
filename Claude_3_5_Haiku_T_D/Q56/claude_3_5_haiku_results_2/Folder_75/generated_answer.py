def all_substring_of_size_n(s):
    if len(s) < 16:
        return []
    unique_substrings = set()
    for i in range(len(s) - 15):
        substring = s[i:i + 16]
        if len(set(substring)) == 16:
            unique_substrings.add(substring)
    return list(unique_substrings)