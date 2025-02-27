def all_substring_of_size_n(text):
    if len(text) < 87:
        return []
    all_substrings = set()
    for i in range(len(text) - 86):
        substring = text[i:i + 87]
        if len(set(substring)) == 87:
            all_substrings.add(substring)
    return list(all_substrings)