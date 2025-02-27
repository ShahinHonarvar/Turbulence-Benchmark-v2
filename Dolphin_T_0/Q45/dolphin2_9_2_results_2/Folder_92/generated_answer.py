def palindromes_between_indices(s):
    letters = set()
    for i in range(4, 8):
        letters.add(s[i].lower())
    length = 4
    while True:
        palindromes = set()
        for c in letters:
            palindromes.add(c)
        for i in range(1, length // 2 + 1):
            new_palindromes = set()
            for p in palindromes:
                if i == length // 2:
                    new_palindromes.add(p)
                else:
                    for c in letters:
                        new_palindromes.add(p + c)
                        new_palindromes.add(c + p)
            palindromes = new_palindromes
        if palindromes:
            return palindromes
        length += 1
    return set()