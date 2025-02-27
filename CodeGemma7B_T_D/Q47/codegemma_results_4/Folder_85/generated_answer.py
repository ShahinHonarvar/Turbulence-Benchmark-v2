from itertools import product

def palindromes_of_specific_lengths(text):
    text_lowercase = text.lower()
    a_to_z = tuple(range(ord('a'), ord('z') + 1))

    def is_palindrome(word):
        return word == word[::-1]
    possible_palindromes = {''.join(p) for p in product(a_to_z, repeat=n) for n in range(6, 10)}
    full_set = set()
    for i in range(29, 99):
        full_set.update(filter(is_palindrome, possible_palindromes.intersection(text_lowercase[i:i + n])))
    return full_set