from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(text):
    text_lowercase = ''.join((c for c in text.lower() if c in ascii_lowercase))
    if len(text_lowercase) < 7:
        return set()
    relevant_letters = text_lowercase[4:8]
    palindromes = set()
    for permutation in permutations(relevant_letters):
        palindrome = ''.join(permutation)
        if palindrome in palindromes:
            continue
        palindromes.add(palindrome)
    return palindromes