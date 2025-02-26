from itertools import permutations

def palindromes_between_indices(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    letters = ''.join(filter(lambda x: x.lower() in alphabet, s[4:8].lower()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, min_length):
        result = set()
        for i in range(min_length, len(chars) + 1):
            for perm in permutations(chars, i):
                word = ''.join(perm)
                if is_palindrome(word):
                    result.add(word)
        return result
    return generate_palindromes(letters, 4)