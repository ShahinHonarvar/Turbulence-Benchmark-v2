from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, 9):
        for j in range(i, 9):
            substring = s[i - 1:j].lower()
            if len(substring) >= 4 and set(substring) <= english_letters:
                for k in range(len(substring) // 2):
                    if substring[k] != substring[-k - 1]:
                        break
                else:
                    palindromes.add(substring)
    return palindromes