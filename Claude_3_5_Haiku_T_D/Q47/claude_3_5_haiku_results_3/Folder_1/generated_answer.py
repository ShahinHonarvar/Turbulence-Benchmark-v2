def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_alphabetic(word):
        return word.isalpha()
    palindromes = set()
    for length in range(40, 73):
        for start in range(15, 90 - length + 1):
            substring = s[start:start + length].lower()
            if is_palindrome(substring) and is_alphabetic(substring):
                palindromes.add(substring)
    return palindromes