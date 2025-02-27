def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join(filter(str.isalpha, s)).lower()
    english_letters = get_english_letters(s[1:6])
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 4, len(english_letters) + 1):
            if is_palindrome(english_letters[i:j]):
                palindromes.add(english_letters[i:j])
    return palindromes