def all_substring_of_size_n(s):
    if len(set(s)) < 99:
        return []
    substrings = []
    for i in range(len(s)):
        for j in range(i + 99, len(s) + 1):
            if len(set(s[i:j])) == 99:
                substrings.append(s[i:j])
    return list(set(substrings))