from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[1:5]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    counter = Counter(letters)
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            palindrome = ''.join(perm)
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes