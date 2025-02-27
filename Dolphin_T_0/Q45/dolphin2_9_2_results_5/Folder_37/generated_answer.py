from itertools import permutations

def palindromes_between_indices(s):
    letters = s[1:5]
    palindrome_length = 5

    def create_palindromes(letters, length):
        result = set()
        for p in permutations(letters, length):
            word = ''.join(p).lower()
            if word == word[::-1]:
                result.add(word)
        return result
    sets = create_palindromes(letters, palindrome_length)
    return sets