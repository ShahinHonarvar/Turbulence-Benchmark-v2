from collections import defaultdict

def palindromes_between_indices(s):
    eng_letters = set()
    for i in range(2, 5):
        for j in range(len(s) - i):
            if s[j:j + i].isalpha() and s[j].lower() in 'abcdefghijklmnopqrstuvwxyz':
                eng_letters.add(s[j:j + i].lower())
    palindromes = set()
    for word in eng_letters:
        if len(word) >= 4:
            palindromes.add(word)
    return palindromes