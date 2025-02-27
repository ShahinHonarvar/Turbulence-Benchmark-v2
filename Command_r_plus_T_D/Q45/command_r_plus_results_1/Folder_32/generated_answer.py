def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word.lower() == word.lower()[::-1]
    result = set()
    for i in range(1, min(8, len(s))):
        substring = s[1:i + 1]
        english_letters = ''.join(filter(str.isalpha, substring))
        if len(english_letters) >= 5 and is_palindrome(english_letters):
            result.add(english_letters)
    return result