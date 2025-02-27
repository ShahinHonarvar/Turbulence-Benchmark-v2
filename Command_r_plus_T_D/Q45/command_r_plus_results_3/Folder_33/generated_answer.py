def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def is_english_letter(char: str) -> bool:
        return char.isalpha()
    palindromes = set()
    substring = s[7:10]
    english_letters = ''.join((char for char in substring if is_english_letter(char)))
    english_letters = english_letters.lower()
    for i in range(len(english_letters)):
        for j in range(i + 4, len(english_letters) + 1):
            sub_palindrome = english_letters[i:j]
            if is_palindrome(sub_palindrome):
                palindromes.add(sub_palindrome)
    return palindromes