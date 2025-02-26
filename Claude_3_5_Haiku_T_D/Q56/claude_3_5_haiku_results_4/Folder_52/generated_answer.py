def all_substring_of_size_n(s):
    if len(s) < 15:
        return []
    unique_substrings = set()
    for i in range(len(s) - 14):
        substring = s[i:i + 15]
        if len(set(substring)) == 15:
            unique_substrings.add(substring)
    return list(unique_substrings)