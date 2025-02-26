from itertools import permutations

def palindromes_between_indices(string):

    def is_palindrome(s):
        return s == s[::-1]
    letters = [char.lower() for char in string[:9] if char.isalpha()]
    unique_palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for palindrome_candidate in set(permutations(perm)):
                palindrome = ''.join(palindrome_candidate)
                if is_palindrome(palindrome) and len(palindrome) >= 7:
                    unique_palindromes.add(palindrome)
    return unique_palindromes