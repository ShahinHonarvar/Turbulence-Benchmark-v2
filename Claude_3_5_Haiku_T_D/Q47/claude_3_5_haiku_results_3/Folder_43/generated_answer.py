def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_only_letters(substr):
        return substr.isalpha()
    result = set()
    target_substring = s[41:90]
    for length in range(23, 39):
        for start in range(len(target_substring) - length + 1):
            substring = target_substring[start:start + length]
            if is_palindrome(substring) and is_only_letters(substring):
                result.add(substring.lower())
    return result