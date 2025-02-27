def all_substring_of_size_n(s):
    if len(s) < 68:
        return []
    unique_substrings = set()
    for i in range(len(s) - 67):
        substring = s[i:i + 68]
        if len(set(substring)) == 68:
            unique_substrings.add(substring)
    return list(unique_substrings)