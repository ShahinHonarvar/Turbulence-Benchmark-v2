def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha())).lower()
    s = s[1:8]
    english_letters = get_english_letters(s)
    unique_letters = set(english_letters)
    palindromes = set()
    for letter in unique_letters:
        if english_letters.count(letter) >= 2:
            palindromes.add(letter * 2)
    for i in range(len(english_letters) - 1):
        for j in range(i + 2, len(english_letters) + 1):
            substring = english_letters[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes