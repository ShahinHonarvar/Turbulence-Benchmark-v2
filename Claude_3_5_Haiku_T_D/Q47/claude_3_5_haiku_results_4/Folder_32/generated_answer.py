def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_only_letters(substring):
        return substring.isalpha()
    target_range = s[16:78]
    palindromes = set()
    for length in range(43, 48):
        for start in range(len(target_range) - length + 1):
            substring = target_range[start:start + length]
            if is_palindrome(substring) and is_only_letters(substring):
                palindromes.add(substring.lower())
    return palindromes