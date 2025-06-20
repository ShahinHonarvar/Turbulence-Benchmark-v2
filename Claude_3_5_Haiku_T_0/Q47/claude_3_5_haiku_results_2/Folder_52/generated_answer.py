def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_only_letters(word):
        return word.isalpha()
    palindromes = set()
    for length in range(13, 43):
        for start in range(44, 100 - length + 1):
            substring = s[start:start + length].lower()
            if is_palindrome(substring) and is_only_letters(substring):
                palindromes.add(substring)
    return palindromes