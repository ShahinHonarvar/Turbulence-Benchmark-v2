def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def contains_only_letters(substring):
        return substring.isalpha()
    palindromes = set()
    substring = s[125:284].lower()
    for length in range(109, 127):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and contains_only_letters(candidate):
                palindromes.add(candidate)
    return palindromes