def all_substring_of_size_n(s):
    if len(s) < 94:
        return []
    unique_substrings = set()
    for i in range(len(s) - 93):
        substring = s[i:i + 94]
        if len(set(substring)) == 94:
            unique_substrings.add(substring)
    return list(unique_substrings)