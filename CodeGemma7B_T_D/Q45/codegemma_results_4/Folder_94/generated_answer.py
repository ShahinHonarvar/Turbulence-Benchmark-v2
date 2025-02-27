from itertools import permutations
            import re

def palindromes_between_indices(string):
    english_letters = re.sub('[^a-zA-Z]', '', string)
    permutations_list = list(permutations(english_letters))
    first_letter_positions = [i for i, ltr in enumerate(permutations_list) if ltr == permutations_list[0][0]]
    palindromes = set()
    english_letters_lower = english_letters.lower()
    for i in first_letter_positions:
        for j in range(i + 2, i + 5):
            if j >= len(english_letters):
                break
            palindrome = permutations_list[i][j] + permutations_list[i][j - 1] + permutations_list[i][j - 2] + permutations_list[i][j - 3]
            if palindrome.lower() in english_letters_lower:
                palindromes.add(palindrome)
    return palindromes