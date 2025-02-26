def all_substring_of_size_n(s):
    if len(s) < 87:
        return []
    unique_substrings = set()
    for i in range(len(s) - 86):
        substring = s[i:i + 87]
        if len(set(substring)) == 87:
            unique_substrings.add(substring)
    return list(unique_substrings)