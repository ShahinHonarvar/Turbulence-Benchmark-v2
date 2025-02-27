def all_substring_of_size_n(s):
    length = 105
    if len(s) < length:
        return []
    substrings = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(set(substring)) == length and substring not in substrings:
            substrings.add(substring)
    return list(substrings)