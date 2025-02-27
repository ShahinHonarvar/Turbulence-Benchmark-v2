from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join([char for char in text[1:5] if char.isalpha()]).lower()
    palindromes = set()
    for perm in permutations(letters):
        palindrome = ''.join(perm) + ''.join(perm[::-1])
        if len(palindrome) >= 5:
            palindromes.add(palindrome)
    return palindromes