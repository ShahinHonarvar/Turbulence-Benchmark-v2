from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, 6):
        for j in range(i, 6):
            substring = s[i - 1:j + 1].lower()
            if len(substring) >= 6 and set(substring) <= english_letters:
                palindromes.add(substring[::-1] + substring[1:-1] + substring[:-1])
    return palindromes