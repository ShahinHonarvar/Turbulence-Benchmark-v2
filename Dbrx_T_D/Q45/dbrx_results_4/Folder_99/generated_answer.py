def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(4, 9):
        for j in range(i, 9):
            substring = s[i:j + 1].lower()
            if english_letters.issuperset(substring) and set(substring) == english_letters.intersection(set(substring)):
                palindromes.add(s[i:j + 1])
    return {p for p in palindromes if len(p) >= 3}