def all_substring_of_size_n(s):
    if len(s) < 19:
        return []
    substrings = set()
    for i in range(len(s) - 19 + 1):
        substring = s[i:i + 19]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)