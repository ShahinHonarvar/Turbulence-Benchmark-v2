def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def is_only_letters(substring):
        return substring.isalpha()
    result = set()
    substring = s[127:289].lower()
    for length in range(119, 142):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_only_letters(candidate):
                result.add(candidate)
    return result