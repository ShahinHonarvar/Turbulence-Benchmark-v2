def palindromes_between_indices(s):
    letters = ''.join(sorted(s[1:6].lower()))
    A = list(map(list, zip(letters, letters[::-1])))
    palindromes = set()
    for p in range(len(A)):
        for q in range(p, len(A)):
            if len(A[p][0] + A[q][0]) >= 6:
                palindromes.add(A[p][0] + A[q][0])
    return palindromes