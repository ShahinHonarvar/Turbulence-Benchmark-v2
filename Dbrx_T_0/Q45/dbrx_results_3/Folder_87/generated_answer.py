from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(3, 10):
        for j in range(i, 10):
            substring = s[3:10][i - j:]
            substring = ''.join((c for c in substring if c.lower() in english_letters))
            if len(substring) >= 3:
                for k in range(len(substring) // 2 + 1):
                    if substring[k] == substring[-k - 1] or (substring[k].lower() == substring[-k - 1].lower() and substring[k] != substring[-k - 1]):
                        palindromes.add(substring[k:-k])
    return palindromes