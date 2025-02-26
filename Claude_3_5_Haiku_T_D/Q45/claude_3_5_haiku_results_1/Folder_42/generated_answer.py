from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[6:10] if char.isalpha()]
    if len(letters) < 3:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            potential_palindrome = list(perm[i:] + perm[:i])
            if len(potential_palindrome) >= 3:
                left = 0
                right = len(potential_palindrome) - 1
                is_palindrome = True
                while left < right:
                    if potential_palindrome[left] != potential_palindrome[right]:
                        is_palindrome = False
                        break
                    left += 1
                    right -= 1
                if is_palindrome:
                    unique_palindromes.add(''.join(potential_palindrome))
    return unique_palindromes