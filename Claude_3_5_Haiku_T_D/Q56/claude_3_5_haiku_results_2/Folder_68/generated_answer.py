def all_substring_of_size_n(s):
    if len(s) < 75:
        return []
    unique_substrings = set()
    for i in range(len(s) - 74):
        substring = s[i:i + 75]
        if len(set(substring)) == 75:
            unique_substrings.add(substring)
    return list(unique_substrings)