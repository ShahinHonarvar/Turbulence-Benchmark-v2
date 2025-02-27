def all_substring_of_size_n(s):
    if len(s) < 99:
        return []
    substrings = set()
    for i in range(len(s) - 98):
        substring = s[i:i + 99]
        if len(set(substring)) == 99:
            substrings.add(substring)
    return list(substrings)