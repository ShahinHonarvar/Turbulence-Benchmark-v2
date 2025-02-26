def all_substring_of_size_n(s):
    if len(s) < 12:
        return []
    unique_substrings = set()
    for i in range(len(s) - 11):
        substring = s[i:i + 12]
        if len(set(substring)) == 12:
            unique_substrings.add(substring)
    return list(unique_substrings)