def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    result = set()
    for i in range(1, 5):
        for j in range(i + 1, 5):
            substring = s[i:j]
            english_letters = ''.join(filter(str.isalpha, substring))
            if len(english_letters) >= 4 and is_palindrome(english_letters.lower()):
                result.add(english_letters)
    return result