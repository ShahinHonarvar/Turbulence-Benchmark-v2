def all_substring_of_size_n(s):
    if len(s) < 40:
        return []
    unique_substrings = set()
    for i in range(len(s) - 39):
        substring = s[i:i + 40]
        if len(set(substring)) == 40:
            unique_substrings.add(substring)
    return list(unique_substrings)