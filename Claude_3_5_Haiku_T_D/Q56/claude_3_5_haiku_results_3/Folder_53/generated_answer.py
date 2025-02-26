def all_substring_of_size_n(s):
    if len(s) < 25:
        return []
    unique_substrings = set()
    for i in range(len(s) - 24):
        substring = s[i:i + 25]
        if len(set(substring)) == 25:
            unique_substrings.add(substring)
    return list(unique_substrings)