import itertools

def palindromes_between_indices(text):
    if len(text) < 5:
        return set()
    letters = []
    for i in range(2, 5):
        if text[i].isalpha():
            letters.append(text[i].lower())
    if not letters:
        return set()
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if palindrome not in palindromes:
            palindromes.add(palindrome)
    return palindromes