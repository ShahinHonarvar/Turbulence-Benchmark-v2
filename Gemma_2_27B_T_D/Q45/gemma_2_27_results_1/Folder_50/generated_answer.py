from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join([char for char in text[4:9] if char.isalpha()]).lower()
    palindromes = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 5:
            palindromes.add(perm_str)
    return palindromes