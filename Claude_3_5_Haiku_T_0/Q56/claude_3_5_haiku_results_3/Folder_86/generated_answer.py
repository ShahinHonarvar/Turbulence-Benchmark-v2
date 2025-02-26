def all_substring_of_size_n(s):
    if len(s) < 143:
        return []
    unique_substrings = set()
    for i in range(len(s) - 142):
        substring = s[i:i + 143]
        if len(set(substring)) == 143:
            unique_substrings.add(substring)
    return list(unique_substrings)