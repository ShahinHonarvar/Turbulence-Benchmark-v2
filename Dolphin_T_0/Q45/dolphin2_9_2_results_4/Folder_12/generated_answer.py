def palindromes_between_indices(s):
    letters = set([c for c in s[3:9] if c.isalpha()])
    palindromes = set()
    for a in letters:
        for b in letters:
            for c in letters:
                for d in letters:
                    word = a + b + c + d
                    if len(set(word)) == len(word) and word == word[::-1]:
                        palindromes.add(word.lower())
    return palindromes