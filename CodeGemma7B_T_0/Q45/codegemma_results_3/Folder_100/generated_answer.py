import re
    from itertools import permutations

def palindromes_between_indices(text):

    def is_palindrome(word):
        return word == word[::-1]

    def get_letters_in_range(text, start, end):
        return re.findall('[a-zA-Z]', text[start:end + 1])

    def generate_palindromes(letters):
        permutations_of_letters = permutations(letters)
        return {''.join(p) for p in permutations_of_letters if is_palindrome(p)}
    letters = get_letters_in_range(text, 0, 5)
    palindromes = generate_palindromes(letters)
    return palindromes