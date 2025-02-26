def palindromes_of_specific_lengths(s):

    def is_letter_only(substring):
        return substring.isalpha()

    def is_palindrome(substring):
        return substring == substring[::-1]
    substring = s[31:75].lower()
    result = set()
    for length in range(23, 40):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_letter_only(candidate) and is_palindrome(candidate):
                result.add(candidate)
    return result