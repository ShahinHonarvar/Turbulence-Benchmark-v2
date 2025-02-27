from collections import defaultdict

def palindromes_between_indices(s):

    def is_palindrome(arr):
        return arr == arr[::-1]

    def get_letters_in_range():
        return {s[i].lower() for i in range(6, 10)}

    def get_possibilities(letters):
        poss = [x for x in itertools.product(letters, repeat=3)]
        return [x for x in poss if is_palindrome(x)]
    letters = get_letters_in_range()
    if not letters.issubset(ENGLISH_LETTERS):
        return set()
    possibilities = get_possibilities(letters)
    return set((''.join(x) for x in possibilities))