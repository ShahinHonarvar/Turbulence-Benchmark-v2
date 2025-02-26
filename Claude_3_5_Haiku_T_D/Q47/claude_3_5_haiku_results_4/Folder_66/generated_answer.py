def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_letters_only(substr):
        return substr.isalpha()
    palindromes = set()
    substring = s[32:80]
    for length in range(35, 42):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate) and is_letters_only(candidate):
                palindromes.add(candidate.lower())
    return palindromes