from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(5, 9):
        for j in range(i, 9):
            substring = s[i:j + 1]
            if set(substring) <= english_letters:
                substring = ''.join(sorted(substring))
                reversed_substring = substring[::-1]
                if substring == reversed_substring:
                    palindromes.add(substring)
    return palindromes