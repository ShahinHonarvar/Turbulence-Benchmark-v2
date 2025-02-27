from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(string):
        return string == string[::-1]
    letters = [char for char in s[1:3].lower() if char.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in permutations(letters, r):
            palindrome = ''.join(perm)
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes