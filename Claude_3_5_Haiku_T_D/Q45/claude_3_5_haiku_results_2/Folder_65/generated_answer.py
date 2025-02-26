from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [char.lower() for char in s[:7] if char.isalpha()]

    def generate_palindromes(letters):
        unique_palindromes = set()
        n = len(letters)
        for length in range(5, n + 1):
            for perm in set(permutations(letters, length)):
                for i in range(length):
                    candidate = list(perm)
                    left = candidate[:i] + candidate[i + 1:]
                    right = left[::-1]
                    palindrome = candidate[i:i + 1] + left + right
                    if is_palindrome(''.join(palindrome)):
                        unique_palindromes.add(''.join(palindrome))
        return unique_palindromes
    return generate_palindromes(letters)