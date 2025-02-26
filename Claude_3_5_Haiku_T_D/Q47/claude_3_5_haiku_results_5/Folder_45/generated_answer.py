def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_letters_only(substr):
        return substr.isalpha()
    result = set()
    substring = s[70:141]
    for length in range(3, 61):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_letters_only(candidate):
                result.add(candidate.lower())
    return result