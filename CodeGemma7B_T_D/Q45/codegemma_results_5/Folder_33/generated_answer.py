from itertools import permutations

def palindromes_between_indices(text):
    letters = [l.lower() for l in text[7:10]]
    permutations_list = list(permutations(letters))
    palindromes = set()
    for p in permutations_list:
        palindrome = ''.join(p)
        if len(palindrome) >= 4:
            palindromes.add(palindrome)
    return palindromes