def all_substring_of_size_n(s):
    if len(s) < 78:
        return []
    unique_substrings = set()
    for i in range(len(s) - 77):
        substring = s[i:i + 78]
        if len(set(substring)) == 78:
            unique_substrings.add(substring)
    return list(unique_substrings)