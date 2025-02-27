def all_substring_of_size_n(s):
    if len(s) < 73:
        return []
    substrings = set()
    for i in range(len(s) - 73 + 1):
        sub = s[i:i + 73]
        if len(set(sub)) == 73:
            substrings.add(sub)
    return list(substrings)