from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(1, min(7, len(s)) + 1):
        for j in range(i, min(7, len(s)) + 1):
            substring = s[i - 1:j]
            letters = set(substring) & english_letters
            if len(letters) < 2:
                continue
            combo = [''] * len(letters)
            for letter in letters:
                combo[letters.index(letter)] = letter
                pal = ''.join(combo)
                if len(pal) >= 4 and pal == pal[::-1]:
                    palindromes.add(pal)
    return palindromes