def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def contains_only_letters(word):
        return word.isalpha()
    palindromes = set()
    for start in range(17, len(s) - 50 + 1):
        for length in range(50, 52):
            substring = s[start:start + length].lower()
            if len(substring) == length and is_palindrome(substring) and contains_only_letters(substring):
                palindromes.add(substring)
    return palindromes