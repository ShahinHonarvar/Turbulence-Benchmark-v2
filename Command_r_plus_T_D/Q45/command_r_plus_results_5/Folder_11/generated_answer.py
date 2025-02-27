def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    chars_between_indices = set(s[3:8]).intersection(english_letters)
    palindromes = set()
    for p_length in range(4, len(chars_between_indices) + 1):
        for p in itertools.permutations(chars_between_indices, p_length):
            if is_palindrome(''.join(p)):
                palindromes.add(''.join(p))
    return palindromes