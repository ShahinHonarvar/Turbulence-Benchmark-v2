from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(2, max(10, len(s))):
        for j in range(2, i + 1):
            substring = s[i - j + 1:i + 1].lower()
            if set(substring).issubset(english_letters):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return {p for p in palindromes if len(p) >= 6}