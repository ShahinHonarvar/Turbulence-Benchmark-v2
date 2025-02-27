def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(1, 6):
        substring = s[0:i]
        letters = set(substring.lower())
        if letters.issubset(english_letters):
            for j in range(i, len(s) + 1):
                word = s[i:j]
                if is_palindrome(word) and len(word) >= 5:
                    palindromes.add(word)
    return palindromes