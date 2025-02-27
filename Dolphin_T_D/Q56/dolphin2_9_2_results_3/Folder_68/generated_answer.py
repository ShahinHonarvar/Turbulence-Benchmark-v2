def all_substring_of_size_n(s):
    if len(s) < 75:
        return []
    substrings = set()
    for i in range(len(s) - 74):
        if len(set(s[i:i + 75])) == 75:
            substrings.add(s[i:i + 75])
    return list(substrings)