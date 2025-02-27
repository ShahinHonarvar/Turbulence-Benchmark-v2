def all_substring_of_size_n(s):
    if len(s) < 18:
        return []
    substrings = set()
    for i in range(len(s) - 17):
        substring = s[i:i + 18]
        if len(set(substring)) == 18:
            substrings.add(substring)
    return list(substrings)