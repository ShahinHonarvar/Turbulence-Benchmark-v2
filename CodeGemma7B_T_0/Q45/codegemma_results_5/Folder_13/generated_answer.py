import itertools
    from string import ascii_lowercase

def palindromes_between_indices(text):

    def is_palindrome(text):
        return text == text[::-1]

    def get_letters_in_range(text):
        return [char for char in text[3:10] if char in ascii_lowercase]

    def generate_permutations(letters):
        return itertools.permutations(letters)

    def create_palindromes(permutations):
        return {''.join(perm) for perm in permutations if is_palindrome(''.join(perm))}
    letters = get_letters_in_range(text.lower())
    permutations = generate_permutations(letters)
    palindromes = create_palindromes(permutations)
    return palindromes