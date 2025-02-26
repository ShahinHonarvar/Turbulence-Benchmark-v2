def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    substring = s[155:284]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 104, min(i + 121, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            if potential_palindrome.isalpha() and is_palindrome(potential_palindrome):
                result.add(potential_palindrome)
    return result