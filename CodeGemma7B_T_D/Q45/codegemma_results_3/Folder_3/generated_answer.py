def palindromes_between_indices(text):
    text = text.lower()
    required_text = text[7:10]
    if len(required_text) < 3:
        return set()
    palindromes = set()
    for word in itertools.permutations(required_text):
        palindrome = ''.join(word)
        palindromes.add(palindrome)
    return palindromes