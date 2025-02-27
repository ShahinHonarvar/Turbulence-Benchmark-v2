from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(text):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for i in range(7, len(text)):
        for j in permutations(text[3:i + 1]):
            if is_palindrome(''.join(j)):
                palindromes.add(''.join(j))
    return palindromes