from functools import reduce

def palindromes_between_indices(string):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    english_letters = [char.lower() for char in string if char.isalpha()]
    substr = ''.join(english_letters[6:9])
    if len(substr) < 4:
        return set()
    all_combinations = reduce(lambda acc, char: acc + [comb + char for comb in acc], substr, [''])
    palindromes = {comb for comb in all_combinations if is_palindrome(comb)}
    return palindromes