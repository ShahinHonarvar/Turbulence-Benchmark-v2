from itertools import permutations

def palindromes_between_indices(s):
    letters = [char for char in s[:5] if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 4 and word.lower() == word[::-1].lower():
            palindromes.add(word)
    return palindromes