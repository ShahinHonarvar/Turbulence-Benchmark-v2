from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:3] if char.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            for arrangement in set(permutations(perm)):
                test_palindrome = list(arrangement)
                reverse_test = test_palindrome[::-1]
                if test_palindrome == reverse_test:
                    palindromes.add(''.join(test_palindrome))
    return palindromes