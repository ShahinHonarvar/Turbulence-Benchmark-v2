def palindromes_between_indices(s):
    chars = sorted(set(s[0:3].lower()))
    length = 3
    res = set()
    while length <= len(s):
        for p in itertools.permutations(chars, length):
            word = ''.join(p)
            if word == word[::-1] and len(word) >= 3:
                res.add(word)
        length += 1
    return res