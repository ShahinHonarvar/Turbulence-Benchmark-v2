def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_only_letters(substr):
        return substr.isalpha()
    palindromes = set()
    substring = s[100:301]
    for length in range(50, 101):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_only_letters(candidate):
                palindromes.add(candidate.lower())
    return palindromes