from itertools import permutations

def palindromes_between_indices(mystr):
    mystr = mystr.lower()
    myslice = mystr[0:7]
    letters = [l for l in myslice if l in 'abcdefghijklmnopqrstuvwxyz']
    if not letters:
        return set()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = {''.join(p) for p in permutations(letters) if is_palindrome(''.join(p))}
    return palindromes