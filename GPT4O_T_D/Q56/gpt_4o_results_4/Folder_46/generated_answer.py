def all_substring_of_size_n(s):
    if len(s) < 87:
        return []
    substrings = set()
    for i in range(len(s) - 86):
        sub = s[i:i + 87]
        if len(set(sub)) == 87:
            substrings.add(sub)
    return list(substrings)