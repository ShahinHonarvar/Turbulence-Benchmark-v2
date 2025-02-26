def all_substring_of_size_n(s):
    if len(s) < 69:
        return []
    unique_substrings = set()
    for i in range(len(s) - 68):
        substring = s[i:i + 69]
        if len(set(substring)) == 69:
            unique_substrings.add(substring)
    return list(unique_substrings)