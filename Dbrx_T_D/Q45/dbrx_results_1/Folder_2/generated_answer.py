from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substr = s[1:6]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i, len(substr) + 1):
            if substr[i:j] and set(substr[i:j]) <= english_letters:
                pal = ''.join(sorted(substr[i:j]))
                if len(pal) >= 6 and pal == pal[::-1]:
                    palindromes.add(pal)
    return palindromes