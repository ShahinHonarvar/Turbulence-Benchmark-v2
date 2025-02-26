def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_letters_only(substring):
        return substring.isalpha()
    palindromes = set()
    substring = s[63:71]
    for length in range(4, 6):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate) and is_letters_only(candidate):
                palindromes.add(candidate.lower())
    return palindromes