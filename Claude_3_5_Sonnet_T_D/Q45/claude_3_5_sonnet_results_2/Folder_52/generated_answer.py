from itertools import permutations

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[:8] if c.isalpha()]

    def is_palindrome(s):
        return s == s[::-1]

    def generate_palindromes(chars, min_length):
        result = set()
        for i in range(min_length, len(chars) + 1):
            for perm in permutations(chars, i):
                word = ''.join(perm)
                if is_palindrome(word):
                    result.add(word)
        return result
    return generate_palindromes(letters, 6)