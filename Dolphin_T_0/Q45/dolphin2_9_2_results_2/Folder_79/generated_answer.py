def palindromes_between_indices(S):
    A = set()
    S = [i for i in S[1:8] if i.isalpha()]
    L = len(S)
    i = 0
    ans = set()
    while i < L:
        j = i + 2
        while j <= L:
            if len(set(sorted([*S[i:j]])) - set('abcdefghijklmnopqrstuvwxyz')) != 0:
                if sorted([*S[i:j]])[::-1] == sorted([*S[i:j]]) and len([*S[i:j]]) >= 3:
                    A.add(''.join(sorted([*S[i:j]])))
            j += 1
        i += 1
    s = set(map(str.lower, map(str.join, map(sorted, A))))
    return s