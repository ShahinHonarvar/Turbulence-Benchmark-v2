def all_substring_of_size_n(s):
    if len(s) < 50:
        return []
    substrings = set()
    for i in range(len(s) - 49):
        if len(set(s[i:i + 50])) == 50:
            substrings.add(s[i:i + 50])
    return list(substrings)