def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(1, 6):
        substring = s[i]
        if substring in english_letters:
            for j in range(i + 1, 6):
                substring += s[j]
                if substring in english_letters and is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes