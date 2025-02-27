from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substr = s[3:9]
    substr = ''.join((x for x in substr if x in english_letters))
    palindromes = {x for x in {substr[i:j] for i in range(len(substr)) for j in range(i + 5, len(substr) + 1)} if x == x[::-1]}
    return palindromes