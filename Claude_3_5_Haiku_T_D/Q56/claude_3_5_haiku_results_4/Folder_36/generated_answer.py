def all_substring_of_size_n(s):
    if len(s) < 146:
        return []
    unique_substrings = set()
    for i in range(len(s) - 145):
        substring = s[i:i + 146]
        if len(set(substring)) == 146:
            unique_substrings.add(substring)
    return list(unique_substrings)