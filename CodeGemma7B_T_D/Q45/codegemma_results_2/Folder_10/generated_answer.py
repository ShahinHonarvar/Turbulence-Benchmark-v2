from itertools import permutations

def palindromes_between_indices(text):
    set_of_all_palindromes = set()
    possible_letters = [char for char in text if char.isalpha()]
    if len(possible_letters) >= 3:
        for i in range(len(possible_letters) - 2):
            for j in range(i + 1, len(possible_letters) - 1):
                for k in range(j + 1, len(possible_letters)):
                    palindrome = ''.join(permutations(possible_letters[i:k + 1]))
                    set_of_all_palindromes.add(palindrome)
    return set_of_all_palindromes