def palindromes_between_indices(s):
    s = s.lower()
    if len(s) < 8:
        return set()
    eng_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(3, 8):
        for j in range(i, 8):
            substr = s[i:j + 1]
            if substr and eng_letters.issuperset(substr):
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes