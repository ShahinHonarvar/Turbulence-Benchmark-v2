def palindromes_of_specific_lengths(s):

    def is_letter_palindrome(substring):
        return substring.isalpha() and substring == substring[::-1]
    palindromes = set()
    for start in range(11, 97):
        for length in range(45, 53):
            if start + length > len(s):
                break
            substring = s[start:start + length].lower()
            if is_letter_palindrome(substring):
                palindromes.add(substring)
    return palindromes