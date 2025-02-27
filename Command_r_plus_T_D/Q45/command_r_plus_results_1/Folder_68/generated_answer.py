def palindromes_between_indices(s: str) -> set:

    def is_palindrome(s):
        return s == s[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters_between_indices = set(s[1:9]).intersection(english_letters)
    palindromes = set()
    for p in letters_between_indices:
        for q in letters_between_indices:
            for r in letters_between_indices:
                for s_ in letters_between_indices:
                    palindrome = p + q + r + s_
                    if is_palindrome(palindrome):
                        palindromes.add(palindrome)
    return palindromes