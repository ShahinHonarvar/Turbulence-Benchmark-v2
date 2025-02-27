from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    potential_letters = [c for c in s[4:9] if c.lower() in english_letters]
    if not potential_letters:
        return set()
    palindromes = set()
    for permutation in permutations(potential_letters):
        palindrome = ''
        for letter in permutation:
            palindrome += letter
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes