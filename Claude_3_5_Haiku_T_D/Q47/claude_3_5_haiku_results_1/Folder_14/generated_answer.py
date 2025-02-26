def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]

    def is_alpha_only(word):
        return word.isalpha()
    palindromes = set()
    for length in range(6, 9):
        for i in range(10, 75 - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring) and is_alpha_only(substring):
                palindromes.add(substring.lower())
    return palindromes