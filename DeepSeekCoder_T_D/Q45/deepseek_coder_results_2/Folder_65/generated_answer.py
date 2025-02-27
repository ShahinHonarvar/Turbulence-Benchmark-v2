from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[0:7].lower()))
    palindromes = set()
    for perm in permutations(letters, min(len(letters), 5)):
        if is_palindrome(''.join(perm)):
            palindromes.add(''.join(perm))
        if len(letters) > 5:
            for perm in permutations(letters, 6):
                if is_palindrome(''.join(perm)):
                    palindromes.add(''.join(perm))
            for perm in permutations(letters, 7):
                if is_palindrome(''.join(perm)):
                    palindromes.add(''.join(perm))
    return palindromes