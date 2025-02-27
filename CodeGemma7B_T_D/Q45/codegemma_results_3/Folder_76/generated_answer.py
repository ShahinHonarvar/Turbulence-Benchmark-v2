from itertools import permutations

def palindromes_between_indices(string):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    valid_palindromes = set()
    for i in range(1, 5):
        for j in range(i, 5):
            substring = string[i - 1:j + 1]
            if all((char in english_letters for char in substring)):
                permutations_list = list(permutations(substring))
                for permutation in permutations_list:
                    valid_palindromes.add(''.join(permutation).lower())
    return valid_palindromes