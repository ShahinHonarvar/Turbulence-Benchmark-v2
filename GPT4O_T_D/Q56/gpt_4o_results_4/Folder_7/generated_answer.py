def all_substring_of_size_n(s):
    if len(s) < 117:
        return []
    substrings = set()
    for i in range(len(s) - 116):
        substring = s[i:i + 117]
        if len(set(substring)) == 117:
            substrings.add(substring)
    return list(substrings)