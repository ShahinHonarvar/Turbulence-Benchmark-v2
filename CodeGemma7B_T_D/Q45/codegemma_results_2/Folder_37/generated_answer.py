def palindromes_between_indices(text):
    text = text.lower()
    letters = text[1:5]
    required_letters = set('abcdefghijklmnopqrstuvwxyz')
    if not letters.count(required_letters):
        return set()
    permutations = itertools.permutations(letters)
    palindromes = set()
    for permutation in permutations:
        palindrome = ''.join(permutation)
        if palindrome.startswith(permutation[0]) and palindrome.endswith(permutation[0]):
            palindromes.add(palindrome)
    return palindromes