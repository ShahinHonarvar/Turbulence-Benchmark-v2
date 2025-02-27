def palindromes_between_indices(string):
    letter_set = set(string[1:9].lower())
    if len(letter_set) < 3:
        return set()
    return set(filter(lambda s: len(s) >= 6, ''.join(letter_set).lower().palindrome()))