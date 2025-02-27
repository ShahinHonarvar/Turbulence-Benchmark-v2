def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 62):
        substring = s[i:i + 63]
        if len(set(substring)) == 63:
            substrings.add(substring)
    return list(substrings)