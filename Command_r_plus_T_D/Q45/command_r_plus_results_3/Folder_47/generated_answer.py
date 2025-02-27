def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]
    english_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    palindromes = set()
    for i in range(3, 8):
        for j in range(i + 1, 8):
            substring = s[i:j]
            if all((char in english_letters for char in substring)):
                for word in substring.lower().replace(' ', ''):
                    if is_palindrome(word) and len(word) >= 5:
                        palindromes.add(word)
    return palindromes