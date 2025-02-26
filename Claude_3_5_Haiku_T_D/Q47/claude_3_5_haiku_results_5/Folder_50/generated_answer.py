def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_only_letters(substr):
        return substr.isalpha()
    result = set()
    substring = s[36:93]
    for length in range(10, 36):
        for i in range(len(substring) - length + 1):
            current_substr = substring[i:i + length]
            if is_palindrome(current_substr) and is_only_letters(current_substr):
                result.add(current_substr.lower())
    return result