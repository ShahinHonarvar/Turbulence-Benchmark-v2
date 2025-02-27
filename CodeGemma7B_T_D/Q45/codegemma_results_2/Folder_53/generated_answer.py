def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(4, 9):
        for j in range(i + 1, 9):
            for k in range(j + 1, 10):
                for l in range(k + 1, 10):
                    for m in range(l + 1, 10):
                        word = s[i:j + 1] + s[k:l + 1] + s[m:j + 1]
                        if word == word[::-1]:
                            palindromes.add(word)
    if not palindromes:
        return {}
    return palindromes