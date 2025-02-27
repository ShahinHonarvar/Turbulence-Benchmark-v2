from itertools import permutations

def palindromes_between_indices(string):
    palindromes = set()
    letters = [letter for letter in string.lower() if letter.isalpha() and 3 <= string.index(letter) <= 8]
    if len(letters) >= 5:
        for perm in permutations(letters):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes