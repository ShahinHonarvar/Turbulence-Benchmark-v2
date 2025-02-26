def all_substring_of_size_n(s):
    if len(s) < 100:
        return []
    unique_substrings = set()
    for i in range(len(s) - 99):
        substring = s[i:i + 100]
        if len(set(substring)) == 100:
            unique_substrings.add(substring)
    return list(unique_substrings)