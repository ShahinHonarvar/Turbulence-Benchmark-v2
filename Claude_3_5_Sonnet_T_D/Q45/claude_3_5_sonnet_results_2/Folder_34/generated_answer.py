from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[5:8])).lower()

    def generate_palindromes(chars, min_length=4):
        palindromes = set()
        for length in range(min_length, len(chars) + 1):
            for perm in permutations(chars, length):
                word = ''.join(perm)
                if word == word[::-1]:
                    palindromes.add(word)
        return palindromes
    return generate_palindromes(letters)