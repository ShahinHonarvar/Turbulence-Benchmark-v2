def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for i in range(2, len(s)):
        substring = s[2:i + 1]
        english_letters = ''.join(filter(str.isalpha, substring)).lower()
        for j in range(len(english_letters) - 2):
            palindrome = english_letters[j:j + 3]
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes