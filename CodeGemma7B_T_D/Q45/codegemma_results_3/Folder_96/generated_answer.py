def palindromes_between_indices(text):
    text = text.lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    indexes = range(3, 9)
    palindromes = set()
    for permutation in itertools.permutations(text[indexes]):
        if all((letter in english_letters for letter in permutation)):
            palindrome = ''.join(permutation)
            if palindrome not in palindromes:
                palindromes.add(palindrome)
    return palindromes