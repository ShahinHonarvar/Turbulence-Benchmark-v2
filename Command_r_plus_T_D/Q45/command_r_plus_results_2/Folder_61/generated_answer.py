def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[:8].lower()
    letters_in_range = set(s_lower) & english_letters
    for palindrome_length in range(7, 9):
        for palindrome in product(letters_in_range, repeat=palindrome_length):
            if is_palindrome(''.join(palindrome)):
                palindromes.add(''.join(palindrome))
    return palindromes