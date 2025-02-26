from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:5] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letter_list):
        palindromes = set()
        for perm in set(permutations(letter_list)):
            for i in range(len(perm)):
                for j in range(i + 2, len(perm) + 1):
                    candidate = ''.join(perm[i:j])
                    if is_palindrome(candidate):
                        palindromes.add(candidate)
        return {p for p in palindromes if len(p) >= 3}
    return generate_palindromes(letters)