def all_substring_of_size_n(s):
    if len(s) < 90:
        return []
    unique_substrings = set()
    for i in range(len(s) - 89):
        substring = s[i:i + 90]
        if len(set(substring)) == 90:
            unique_substrings.add(substring)
    return list(unique_substrings)