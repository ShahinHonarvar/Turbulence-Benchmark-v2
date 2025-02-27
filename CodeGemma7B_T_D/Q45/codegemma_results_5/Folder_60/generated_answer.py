from itertools import permutations

def palindromes_between_indices(input_string):

    def is_palindrome(word):
        return word == word[::-1]
    english_letters = list('abcdefghijklmnopqrstuvwxyz')
    alphabets_in_input = [char for char in input_string if char in english_letters]
    filtered_alphabets_in_input = [alphabet for alphabet in alphabets_in_input if alphabets_in_input.index(alphabet) >= 3 and alphabets_in_input.index(alphabet) <= 6]
    if filtered_alphabets_in_input:
        return {''.join(map(str, [char for char in palindrome])) for palindrome in permutations(filtered_alphabets_in_input) if is_palindrome(''.join([char for char in palindrome]))}
    else:
        return set()