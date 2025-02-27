def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 75, len(s) + 1):
            if len(set(s[i:j])) == 75 and len(s[i:j]) == 75:
                substrings.append(s[i:j])
    return list(set(substrings))