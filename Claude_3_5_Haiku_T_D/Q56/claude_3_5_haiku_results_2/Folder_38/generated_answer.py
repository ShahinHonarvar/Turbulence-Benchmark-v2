def all_substring_of_size_n(s):
    if len(s) < 35:
        return []
    unique_substrings = set()
    for i in range(len(s) - 34):
        substring = s[i:i + 35]
        if len(set(substring)) == 35:
            unique_substrings.add(substring)
    return list(unique_substrings)