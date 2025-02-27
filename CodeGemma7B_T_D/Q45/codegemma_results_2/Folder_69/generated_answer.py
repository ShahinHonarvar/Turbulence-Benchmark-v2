from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    set_of_palindromes = set()
    for starting_index in range(4):
        for ending_index in range(4):
            if starting_index <= ending_index:
                word = ''.join(permutations(s[starting_index:ending_index + 1], r=ending_index + 1 - starting_index))
                if is_palindrome(word):
                    set_of_palindromes.add(word.lower())
    if set_of_palindromes:
        return set_of_palindromes
    else:
        return set()