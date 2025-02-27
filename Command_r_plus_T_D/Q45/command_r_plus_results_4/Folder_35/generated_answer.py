def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(2, 5):
        if s[i] in english_letters:
            for j in range(i + 1, len(s)):
                if s[j] in english_letters:
                    palindrome = s[i:j + 1]
                    if is_palindrome(palindrome) and len(palindrome) >= 4:
                        palindromes.add(palindrome.lower())
    return palindromes