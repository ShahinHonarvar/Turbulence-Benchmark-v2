import re
  from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    string = string[3:9]
    string = ''.join(re.findall('[a-zA-Z]+', string)).lower()
    letters = Counter(string)
    center = ''
    half_palindrome = ''
    for letter in letters:
        if letters[letter] % 2 == 1:
            if center != '':
                return set()
            center = letter
            letters[letter] -= 1
        if letters[letter] > 0:
            half_palindrome += letter * (letters[letter] // 2)
    if len(half_palindrome) < 3:
        return set()
    perms = set([''.join(p) for p in permutations(half_palindrome)])
    palindromes = set()
    for perm in perms:
        palindromes.add(perm + center + perm[::-1])
    return palindromes