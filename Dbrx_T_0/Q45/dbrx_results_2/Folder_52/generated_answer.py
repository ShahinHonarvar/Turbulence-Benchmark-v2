from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(0, min(8, len(s))):
        for j in range(i, min(8, len(s))):
            substring = s[i:j + 1].lower()
            if set(substring) <= english_letters:
                if len(substring) >= 6 and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes