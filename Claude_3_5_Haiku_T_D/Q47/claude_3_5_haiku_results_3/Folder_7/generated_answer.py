def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_letters_only(substring):
        return substring.isalpha()
    result = set()
    for length in range(104, 124):
        for start in range(119, 257 - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring) and is_letters_only(substring):
                result.add(substring)
    return result