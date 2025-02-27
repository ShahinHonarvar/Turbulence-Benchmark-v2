def all_substring_of_size_n(S):
    L = 142
    D = {}
    for i in range(len(S)):
        S1 = S[i:i + L]
        if len(S1) == L and len(set(S1)) == L:
            D[S1] = 1
    return list(D.keys())