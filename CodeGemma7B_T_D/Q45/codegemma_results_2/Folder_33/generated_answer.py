def palindromes_between_indices(st):
    res = set()
    for i in range(len(st) - 3):
        for j in range(i + 4, len(st)):
            if all([st[k] in 'abcdefghijklmnopqrstuvwxyz' for k in range(i, j + 1)]):
                word = ''.join(sorted([ch for ch in st[i:j + 1] if ch.isalpha()]))
                res.add(word)
    return res