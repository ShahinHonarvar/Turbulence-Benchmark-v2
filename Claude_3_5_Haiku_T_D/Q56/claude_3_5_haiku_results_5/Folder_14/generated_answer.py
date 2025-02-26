def all_substring_of_size_n(s):
    if len(s) < 85:
        return []
    unique_substrings = set()
    for i in range(len(s) - 84):
        substring = s[i:i + 85]
        if len(set(substring)) == 85:
            unique_substrings.add(substring)
    return list(unique_substrings)