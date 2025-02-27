def all_substring_of_size_n(s):
    if len(s) < 105:
        return []
    substrings = set()
    for i in range(0, len(s) - 104):
        substring = s[i:i + 105]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)