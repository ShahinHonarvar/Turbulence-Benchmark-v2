from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:8].lower()
    letters = [char for char in substring if char.isalpha()]

    def generate_palindromes(chars):
        result = set()
        for perm in set(permutations(chars)):
            for length in range(4, len(perm) + 1):
                for start in range(len(perm) - length + 1):
                    candidate = perm[start:start + length]
                    if len(candidate) >= 4:
                        palindrome = candidate + candidate[::-1]
                        if len(palindrome) % 2 == 0 and len(set(palindrome)) == len(palindrome):
                            result.add(''.join(palindrome))
        return result
    return generate_palindromes(letters)