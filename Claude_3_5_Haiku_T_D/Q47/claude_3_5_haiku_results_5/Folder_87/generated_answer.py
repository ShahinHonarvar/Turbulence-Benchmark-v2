def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_only_letters(substr):
        return substr.isalpha()
    palindromes = set()
    for start in range(11, 94):
        for length in range(34, 55):
            if start + length > len(s):
                break
            substring = s[start:start + length]
            if is_palindrome(substring) and is_only_letters(substring):
                palindromes.add(substring)
    return palindromes