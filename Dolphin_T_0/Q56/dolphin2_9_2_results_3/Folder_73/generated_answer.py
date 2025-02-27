def all_substring_of_size_n(s):
    sub = []
    for i in range(len(s) - 1):
        for j in range(i + 2, len(s) + 2):
            if len(s[i:j]) == 20 and len(set(s[i:j])) == 20:
                sub.append(s[i:j])
    return list(set(sub))