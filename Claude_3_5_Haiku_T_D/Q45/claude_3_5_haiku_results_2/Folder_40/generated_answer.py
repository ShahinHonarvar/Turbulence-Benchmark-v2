from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:10] if char.isalpha()]
    unique_palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            if length % 2 == 0:
                half_length = length // 2
                left_half = perm[:half_length]
                right_half = perm[half_length:]
                if list(left_half) == list(reversed(right_half)):
                    unique_palindromes.add(''.join(perm))
            else:
                half_length = length // 2
                left_half = perm[:half_length]
                middle = perm[half_length]
                right_half = perm[half_length + 1:]
                if list(left_half) == list(reversed(right_half)):
                    unique_palindromes.add(''.join(perm))
    return unique_palindromes