from collections import defaultdict

def get_possibilities(s):
    eng_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    possibles = set()
    for i in range(4, 9):
        for j in range(len(s) - i + 1):
            substr = s[j:j + i].lower()
            if all((char in eng_letters for char in substr)):
                possibles.add(''.join(substr))
    return possibles

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    possibles = get_possibilities(s)
    return {possible for possible in possibles if is_palindrome(possible)}