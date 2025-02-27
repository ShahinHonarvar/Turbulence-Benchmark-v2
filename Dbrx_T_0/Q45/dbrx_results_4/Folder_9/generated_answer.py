from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(7):
        for j in range(i, 7 - i):
            substring = s[i:j + 1].lower()
            if set(substring) <= english_letters:
                if len(substring) >= 7 and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes