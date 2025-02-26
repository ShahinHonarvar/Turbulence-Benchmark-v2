from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[2:4] if c.isalpha()))

    def generate_palindromes(chars, min_length=3):
        result = set()
        for i in range(min_length, len(chars) + 1):
            for p in permutations(chars, i):
                word = ''.join(p)
                if word == word[::-1]:
                    result.add(word)
        return result
    return generate_palindromes(letters)