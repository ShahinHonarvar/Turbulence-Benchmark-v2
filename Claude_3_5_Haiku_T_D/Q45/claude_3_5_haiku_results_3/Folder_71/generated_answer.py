from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:4] if char.isalpha()]

    def generate_palindromes(letters):
        palindromes = set()
        for length in range(4, len(letters) * 2 + 1, 2):
            for perm in set(permutations(letters, length // 2)):
                half = list(perm)
                palindrome = half + half[::-1]
                palindromes.add(''.join(palindrome))
        return palindromes
    return generate_palindromes(letters)