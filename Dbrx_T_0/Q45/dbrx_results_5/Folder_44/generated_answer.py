from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(2, 8):
        for j in range(i, 8):
            substring = s[i:j + 1].lower()
            if set(substring) <= english_letters:
                if len(substring) >= 3 and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes