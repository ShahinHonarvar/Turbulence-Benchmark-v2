def palindromes_between_indices(text):
    if not text:
        return set()
    lower_text = text.lower()
    letters = set(lower_text[1:6])
    if len(letters) < 3:
        return set()
    palindromes = set()
    for permutation in itertools.permutations(letters, len(letters)):
        palindrome = ''.join(permutation)
        if palindrome in lower_text:
            palindromes.add(palindrome)
    return palindromes