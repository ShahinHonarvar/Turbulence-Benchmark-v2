def all_substring_of_size_n(s):
    t = []
    for i in range(len(s) - 11 + 1):
        for j in range(i + 11):
            t.append(s[i:j])
    return list(set(t))