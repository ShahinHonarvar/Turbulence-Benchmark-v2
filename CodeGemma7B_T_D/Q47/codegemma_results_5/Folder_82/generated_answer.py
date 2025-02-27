def palindromes_of_specific_lengths(s):
    A = {chr(i + ord('A')) for i in range(26)}
    S = s.upper()
    res = set()
    for i in range(3, len(S) - 2):
        for j in range(i + 26, min(300, len(S)) + 1):
            if S[i:j + 1] == S[i:j + 1][::-1] and S[i:j + 1].issubset(A):
                res.add(S[i:j + 1])
    return res