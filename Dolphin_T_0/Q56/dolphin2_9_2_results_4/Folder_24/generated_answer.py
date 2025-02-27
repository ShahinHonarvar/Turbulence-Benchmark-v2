def all_substring_of_size_n(S):
    res = []
    for i in range(len(S) - 51):
        tmp = S[i:i + 52]
        if len(set(tmp)) == 52:
            res.append(tmp)
    return res