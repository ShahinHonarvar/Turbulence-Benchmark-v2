from collections import defaultdict

def palindromes_between_indices(s):
    eng_letters = frozenset('abcdefghijklmnopqrstuvwxyz')
    letters_in_range = {c.lower() for c in s[2:9]} & eng_letters
    palindromes = set()
    for letters in map(''.join, itertools.product(letters_in_range, repeat=6)):
        if len(letters) != len(set(letters)):
            continue
        palindrome = ''.join(filter(lambda c: c.lower() in letters, s[2:9]))
        if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes