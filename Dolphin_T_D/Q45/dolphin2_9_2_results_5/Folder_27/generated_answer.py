def palindromes_between_indices(s):
    s = s[2:9].lower()
    letters = set(''.join(filter(str.isalpha, s)))
    length = len(letters)
    if length < 3:
        return set()
    palindromes = set()
    for i in range(length, 0, -1):
        for subset in combinations(letters, i):
            word = ''.join(subset)
            if len(word) >= 6 and word == word[::-1]:
                palindromes.add(word)
    return palindromes