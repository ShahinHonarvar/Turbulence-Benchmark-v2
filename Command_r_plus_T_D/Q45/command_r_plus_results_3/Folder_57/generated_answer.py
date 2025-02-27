def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    english_letters = ''.join(filter(str.isalpha, s[2:6].lower()))
    return set((word for word in english_letters for i in range(5, len(english_letters) + 1) if is_palindrome(word[:i])))