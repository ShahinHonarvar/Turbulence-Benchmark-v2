from itertools import permutations
    from string import ascii_letters

def palindromes_between_indices(string):

    def is_palindrome(word):
        return word == word[::-1]
    sub_string = ''.join([char.lower() for char in string[2:7] if char in ascii_letters])
    if len(sub_string) >= 6:
        palindromes = set((''.join(p) for p in permutations(sub_string, len(sub_string)) if is_palindrome(p)))
    else:
        palindromes = set()
    return palindromes