def palindromes_between_indices(s):
    sub = s[6:10]
    sub = sub.lower()
    palindromes = []
    for p in permutations(sub):
        word = ''.join(p)
        if len(word) >= 4 and word == word[::-1]:
            palindromes.append(word)
    return set(palindromes)