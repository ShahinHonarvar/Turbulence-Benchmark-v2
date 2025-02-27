from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[8:10] if c.isalpha()]
    unique_letters = set(letters)
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for p in permutations(letters, length):
            palindrome = ''.join(p).lower()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes