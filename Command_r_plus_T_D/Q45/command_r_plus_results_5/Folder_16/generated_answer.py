def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    english_letters = ''.join(filter(str.isalpha, s[6:10].lower()))
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 4, len(english_letters) + 1):
            if is_palindrome(english_letters[i:j]):
                palindromes.add(english_letters[i:j])
    return palindromes