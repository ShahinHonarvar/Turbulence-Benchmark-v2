def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]

    def is_only_letters(substr):
        return substr.isalpha()
    palindromes = set()
    substring = s[155:284]
    for length in range(104, 121):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length].lower()
            if is_palindrome(candidate) and is_only_letters(candidate):
                palindromes.add(candidate)
    return palindromes