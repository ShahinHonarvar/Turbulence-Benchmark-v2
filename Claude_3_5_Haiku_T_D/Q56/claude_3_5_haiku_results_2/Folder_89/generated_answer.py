def all_substring_of_size_n(s):
    if len(s) < 38:
        return []
    unique_substrings = set()
    for i in range(len(s) - 37):
        substring = s[i:i + 38]
        if len(set(substring)) == 38:
            unique_substrings.add(substring)
    return list(unique_substrings)