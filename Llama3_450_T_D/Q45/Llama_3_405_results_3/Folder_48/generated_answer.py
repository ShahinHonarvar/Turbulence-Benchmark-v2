from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(string):
        return string == string[::-1]
    english_letters = [char.lower() for char in s[6:9] if char.isalpha()]
    palindromes = set()
    for length in range(4, len(english_letters) + 1):
        for p in permutations(english_letters, length):
            palindrome = ''.join(p)
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes