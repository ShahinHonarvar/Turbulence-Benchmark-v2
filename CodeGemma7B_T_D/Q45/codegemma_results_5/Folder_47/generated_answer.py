import itertools

def palindromes_between_indices(text):
    half_range = range(3, 8)
    letters = []
    for i in half_range:
        letters.append(text.lower()[i])
    palindromes = set()
    for permutation in itertools.product(*map(sorted, letters)):
        palindrome = ''.join(list(permutation))
        if len(palindrome) >= 5:
            palindromes.add(palindrome)
    return palindromes