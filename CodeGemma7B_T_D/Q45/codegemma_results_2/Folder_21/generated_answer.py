from itertools import permutations

def palindromes_between_indices(text):
    seven_letters = ''.join(sorted({letter.lower() for letter in text[1:9] if letter.isalpha()}))
    palindromes = set()
    for perm in permutations(seven_letters):
        palindrome = perm[0] + ''.join(perm[1:-1][::-1]) + perm[-1]
        palindromes.add(palindrome)
    return palindromes