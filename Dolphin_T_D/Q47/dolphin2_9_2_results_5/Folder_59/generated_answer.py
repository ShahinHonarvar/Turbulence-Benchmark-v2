def palindromes_of_specific_lengths(S):
    S = S.lower()
    sub = S[:101]
    pal = set()
    for i in range(3, 16):
        for j in range(len(sub) - i + 1):
            subs = sub[j:j + i]
            if subs == subs[::-1] and subs.isalpha():
                pal.add(subs)
    return pal