def all_substring_of_size_n(s):
    if len(s) < 14:
        return []
    substrings = set()
    for i in range(len(s) - 13):
        substring = ''.join(sorted(s[i:i + 14]))
        substrings.add(substring)
    return list(substrings)