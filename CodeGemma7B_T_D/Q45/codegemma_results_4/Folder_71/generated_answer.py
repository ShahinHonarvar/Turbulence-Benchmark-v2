from itertools import permutations

def palindromes_between_indices(word):
    set_of_palindromes = set()
    for item in permutations(word[1:4]):
        palindrome = ''.join(item)
        if palindrome.lower() not in set_of_palindromes:
            set_of_palindromes.add(palindrome.lower())
    return set_of_palindromes