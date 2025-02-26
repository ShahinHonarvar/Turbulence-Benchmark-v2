def all_substring_of_size_n(s):
    if len(s) < 71:
        return []
    unique_substrings = set()
    for i in range(len(s) - 70):
        substring = s[i:i + 71]
        if len(set(substring)) == 71:
            unique_substrings.add(substring)
    return list(unique_substrings)