def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    palindromes = set()
    substring = s[6:10].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substring_letters = set((char for char in substring if char in english_letters))
    for letter in substring_letters:
        if substring.count(letter) >= 2:
            palindrome = letter * 2
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes