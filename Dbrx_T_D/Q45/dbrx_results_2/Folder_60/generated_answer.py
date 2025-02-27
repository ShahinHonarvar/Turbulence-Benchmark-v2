def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s = s.lower()
    palindromes = set()
    for i in range(3, 7):
        for j in range(i, 7):
            substr = s[i:j + 1]
            if english_letters.intersection(set(substr)):
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes