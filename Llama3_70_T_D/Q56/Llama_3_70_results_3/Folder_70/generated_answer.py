def all_substring_of_size_n(s):
    if len(s) < 12:
        return []
    substrings = set()
    for i in range(len(s) - 11):
        substring = s[i:i + 12]
        if len(set(substring)) == 12:
            substrings.add(substring)
    return list(substrings)