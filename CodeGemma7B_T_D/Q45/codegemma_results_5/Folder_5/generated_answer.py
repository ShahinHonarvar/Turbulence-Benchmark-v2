def palindromes_between_indices(text):
    text = text.lower()
    text_range = text[4:9]
    english_letters = set(text_range) - set(string.punctuation + string.whitespace)
    if len(english_letters) < 4:
        return set()
    palindromes = set()
    for permutation in itertools.permutations(english_letters):
        palindrome = ''.join(permutation)
        if palindrome in palindromes:
            continue
        palindromes.add(palindrome)
    return palindromes