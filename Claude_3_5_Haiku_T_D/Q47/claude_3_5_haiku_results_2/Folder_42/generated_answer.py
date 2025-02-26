def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_alphabetic(substring):
        return substring.isalpha()
    palindromes = set()
    if len(s) < 96:
        return palindromes
    substring = s[43:96]
    for length in range(18, 48):
        for i in range(len(substring) - length + 1):
            current_substring = substring[i:i + length]
            if is_palindrome(current_substring) and is_alphabetic(current_substring):
                palindromes.add(current_substring.lower())
    return palindromes