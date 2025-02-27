def all_substring_of_size_n(s):
    if len(s) < 73:
        return []
    substrings = set()
    for i in range(len(s) - 72):
        substring = s[i:i + 73]
        if len(set(substring)) == 73:
            substrings.add(substring)
    return list(substrings)