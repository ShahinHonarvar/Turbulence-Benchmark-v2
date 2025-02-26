def all_substring_of_size_n(s):
    if len(s) < 144:
        return []
    unique_substrings = set()
    for i in range(len(s) - 143):
        substring = s[i:i + 144]
        if len(set(substring)) == 144:
            unique_substrings.add(substring)
    return list(unique_substrings)