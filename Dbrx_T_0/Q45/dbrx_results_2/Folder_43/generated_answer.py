from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(2, 6):
        for j in range(i, 6 - i + 2):
            substr = s[i - 1:j].lower()
            if set(substr) <= english_letters:
                if len(substr) % 2 == 0 and substr[:len(substr) // 2] == substr[len(substr) // 2:][::-1]:
                    palindromes.add(substr)
                elif len(substr) % 2 != 0 and substr[:len(substr) // 2] == substr[len(substr) // 2 + 1:][::-1]:
                    palindromes.add(substr)
    return palindromes