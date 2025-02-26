def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    result = set()
    substring = s[10:71]
    for i in range(len(substring)):
        for j in range(i + 24, min(i + 53, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j]))
            if 24 <= len(potential_palindrome) <= 52 and is_palindrome(potential_palindrome):
                result.add(potential_palindrome)
    return result