from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(string):
        return string == string[::-1]
    letters = [char.lower() for char in s[1:6] if char.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for permutation in permutations(letters, length):
            palindrome = ''.join(permutation)
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes