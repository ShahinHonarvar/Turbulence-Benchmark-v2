def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def is_english_letter(char: str) -> bool:
        return char.lower() in 'abcdefghijklmnopqrstuvwxyz'
    english_letters = ''.join(filter(is_english_letter, s[1:6].lower()))
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 4, len(english_letters) + 1):
            substring = english_letters[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes