def palindromes_between_indices(s):
    letters = ''.join(sorted(set(s[2:6].lower())))
    if len(letters) < 4:
        return set()
    res = set()
    for symmetry in range(0, (len(letters) + 1) // 2):
        for i in range(0, letters.__len__() - symmetry):
            if letters[i] != letters[i + symmetry]:
                break
            else:
                res.add(letters[i:i + symmetry * 2])
    return res