def all_substring_of_size_n(s):
    if len(s) < 70:
        return []
    substrings = set()
    for i in range(len(s) - 69):
        substring = s[i:i + 70]
        if len(set(substring)) == 70:
            substrings.add(substring)
    return list(substrings)