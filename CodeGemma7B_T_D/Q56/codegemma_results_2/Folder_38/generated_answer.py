def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 34):
        mem = set()
        for j in range(i, i + 35):
            if s[j] in mem:
                break
            mem.add(s[j])
        else:
            res.append(s[i:i + 35])
    return res