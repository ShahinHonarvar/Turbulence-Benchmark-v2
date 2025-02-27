def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters = set(s[5:8]) & english_letters
    for letter1 in letters:
        for letter2 in letters:
            palindrome = letter1 + letter2 + letter2 + letter1
            palindromes.add(palindrome)
    return palindromes