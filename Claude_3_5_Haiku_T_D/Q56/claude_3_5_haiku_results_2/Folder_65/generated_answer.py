def all_substring_of_size_n(s):
    if len(s) < 81:
        return []
    unique_substrings = set()
    for i in range(len(s) - 80):
        substring = s[i:i + 81]
        if len(set(substring)) == 81:
            unique_substrings.add(substring)
    return list(unique_substrings)