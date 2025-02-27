def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s_letters = set(s[5:10])
    if not s_letters.issubset(english_letters):
        return set()
    palindromes = set()
    for i in range(5, 10):
        for j in range(i + 1, 10):
            substring = s[i:j]
            if len(substring) >= 5 and substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes