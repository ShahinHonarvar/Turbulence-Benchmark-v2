def all_substring_of_size_n(s):
    if len(s) < 124:
        return []
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 124, len(s) + 1):
            if len(set(s[i:j])) == 124:
                substrings.add(s[i:j])
    return list(substrings)