from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(9):
        for j in range(i, 9):
            substring = s[i:j + 1].lower()
            if len(substring) >= 7 and set(substring) <= english_letters:
                palindromes.add(''.join(sorted(substring)))
    return palindromes