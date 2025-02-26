def all_substring_of_size_n(s):
    if len(s) < 57:
        return []
    unique_substrings = set()
    for i in range(len(s) - 56):
        substring = s[i:i + 57]
        if len(set(substring)) == 57:
            unique_substrings.add(substring)
    return list(unique_substrings)