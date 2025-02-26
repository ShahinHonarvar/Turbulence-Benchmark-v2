def all_substring_of_size_n(s):
    if len(s) < 149:
        return []
    unique_substrings = set()
    for i in range(len(s) - 148):
        substring = s[i:i + 149]
        if len(set(substring)) == 149:
            unique_substrings.add(substring)
    return list(unique_substrings)