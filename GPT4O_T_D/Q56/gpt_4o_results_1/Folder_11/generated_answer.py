def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 77):
        substring = s[i:i + 78]
        if len(substring) == 78 and len(set(substring)) == 78:
            substrings.add(substring)
    return list(substrings)