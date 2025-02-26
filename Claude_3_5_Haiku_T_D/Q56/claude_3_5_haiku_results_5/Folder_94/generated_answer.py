def all_substring_of_size_n(s):
    if len(s) < 70:
        return []
    unique_substrings = set()
    for i in range(len(s) - 69):
        substring = s[i:i + 70]
        if len(set(substring)) == 70:
            unique_substrings.add(substring)
    return list(unique_substrings)