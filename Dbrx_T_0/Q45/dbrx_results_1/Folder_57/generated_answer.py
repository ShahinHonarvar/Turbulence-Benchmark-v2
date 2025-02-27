from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(2, 6):
        for j in range(i, 6):
            substr = s[i:j + 1].lower()
            if set(substr) <= english_letters:
                if len(substr) >= 5 and substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes