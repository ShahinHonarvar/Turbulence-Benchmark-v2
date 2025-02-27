def all_substring_of_size_n(s):
    substrings = set()
    n = len(s)
    for i in range(n - 77):
        substring = s[i:i + 78]
        if len(set(substring)) == 78:
            substrings.add(substring)
    return list(substrings)