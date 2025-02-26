def all_substring_of_size_n(s):
    if len(s) < 36:
        return []
    unique_substrings = set()
    for i in range(len(s) - 35):
        substring = s[i:i + 36]
        if len(set(substring)) == 36:
            unique_substrings.add(substring)
    return list(unique_substrings)