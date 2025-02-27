from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(4, 7):
        for j in range(i, 7 - i + 1):
            substring = s[i - 1:j]
            if set(substring) <= english_letters:
                if len(substring) == 1:
                    palindromes.add(substring)
                elif len(substring) == 2:
                    palindromes.add(substring)
                elif len(substring) == 3:
                    palindromes.add(substring)
                else:
                    for k in range(0, len(substring) - 2, 2):
                        if substring[k] == substring[-k - 1]:
                            palindromes.add(substring[k:-k - 1])
                        else:
                            break
    return palindromes