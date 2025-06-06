def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_english_letters_only(word):
        return word.isalpha()
    palindromes = set()
    for length in range(14, 40):
        for start in range(34, 91 - length + 1):
            substring = s[start:start + length].lower()
            if is_palindrome(substring) and is_english_letters_only(substring):
                palindromes.add(substring)
    return palindromes