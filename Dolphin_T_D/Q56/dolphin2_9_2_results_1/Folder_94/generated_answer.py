def all_substring_of_size_n(s):
    n = len(s)
    if n < 70:
        return []
    substrings = set()
    for i in range(n - 69):
        substring = s[i:i + 70]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)