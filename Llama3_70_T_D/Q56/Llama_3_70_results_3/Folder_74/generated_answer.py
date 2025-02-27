def all_substring_of_size_n(s):
    size_n = 97
    if len(s) < size_n:
        return []
    substrings = set()
    for i in range(len(s) - size_n + 1):
        substring = s[i:i + size_n]
        if len(set(substring)) == size_n:
            substrings.add(substring)
    return list(substrings)