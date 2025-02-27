import random
    import string

def palindromes_between_indices(string):
    substring = string[7:9]
    letters = [c for c in substring if c.isalpha()]
    for length in range(3, len(letters) + 1):
        for subset in combinations(letters, length):
            for permutation in permutations(subset):
                palindrome = ''.join(permutation)
                if palindrome.lower() == palindrome.lower()[::-1] and palindrome not in palindromes:
                    palindromes.add(palindrome)
    return palindromes if palindromes else set()