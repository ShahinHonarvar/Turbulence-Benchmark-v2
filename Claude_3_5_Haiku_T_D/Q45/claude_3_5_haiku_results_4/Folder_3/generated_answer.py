from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[7:10] if char.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        palindrome_set = set()
        for length in range(3, len(letters) + 1):
            for perm in permutations(letters, length):
                for arrangement in set(permutations(perm)):
                    word = ''.join(arrangement)
                    if is_palindrome(word):
                        palindrome_set.add(word)
        return palindrome_set
    return generate_palindromes(letters)