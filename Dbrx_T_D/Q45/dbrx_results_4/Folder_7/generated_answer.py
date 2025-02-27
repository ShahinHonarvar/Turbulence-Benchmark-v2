def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, 10):
        for j in range(i, 10):
            substring = s[i:j + 1].lower()
            if all((letter in english_letters for letter in substring)) and len(substring) >= 7:
                palindromes.add(''.join(sorted(substring)))
    return palindromes