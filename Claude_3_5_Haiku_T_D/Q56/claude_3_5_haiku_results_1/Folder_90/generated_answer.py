def all_substring_of_size_n(s):
    if len(s) < 130:
        return []
    unique_substrings = set()
    for i in range(len(s) - 129):
        substring = s[i:i + 130]
        if len(set(substring)) == 130:
            unique_substrings.add(substring)
    return list(unique_substrings)