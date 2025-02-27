def all_substring_of_size_n(s):
    if len(s) < 43:
        return []
    all_str = []
    for i in range(len(s) - 42):
        for j in range(i + 1, len(s)):
            if len(set(s[i:j + 1])) == 43:
                all_str.append(s[i:j + 1])
    return list(set(all_str))