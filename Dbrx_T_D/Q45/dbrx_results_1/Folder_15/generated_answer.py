from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, min(3, len(s) - 1)):
        for j in range(i, min(3, len(s))):
            substr = s[i:j + 1]
            if set(substr) <= english_letters:
                substr = substr.lower()
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes