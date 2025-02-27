from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(2, 5):
        for j in range(i, 5):
            substring = s[i:j + 1]
            if set(substring) <= english_letters:
                for k in range(len(substring) // 2):
                    if substring[k] != substring[-k - 1]:
                        break
                else:
                    palindromes.add(substring)
    return {p for p in palindromes if len(p) >= 4}