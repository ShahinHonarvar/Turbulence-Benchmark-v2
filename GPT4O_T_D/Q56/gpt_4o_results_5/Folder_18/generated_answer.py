def all_substring_of_size_n(s):
    substrings = set()
    length = len(s)
    for i in range(length - 62):
        substring = s[i:i + 63]
        if len(substring) == 63 and len(set(substring)) == 63:
            substrings.add(substring)
    return list(substrings)