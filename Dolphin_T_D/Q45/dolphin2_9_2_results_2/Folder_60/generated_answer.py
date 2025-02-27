def palindromes_between_indices(s):
    letters = [c for c in s[3:7] if c.isalpha()]
    if len(letters) < 2:
        return set()
    palindromes = set()
    for p in range(4, len(letters) + 4):
        for i in range(len(letters) - p + 1):
            subseq = letters[i:i + p]
            for p in set(map(str.lower, subseq)):
                if not p.isalpha():
                    continue
                pal = p + subseq.count(p) // 2 * p
                n = len(pal)
                m = n // 2
                left = pal[:m]
                right = pal[m:]
                if left == right[::-1]:
                    palindromes.add(pal)
    return palindromes