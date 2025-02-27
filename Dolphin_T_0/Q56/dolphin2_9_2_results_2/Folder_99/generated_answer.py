def all_substring_of_size_n(s):
    length = len(s)
    if length < 110:
        return []
    subsequences = set()
    for i in range(length - 110 + 1):
        substring = s[i:i + 110]
        if len(set(substring)) == 110:
            subsequences.add(substring)
    return list(subsequences)