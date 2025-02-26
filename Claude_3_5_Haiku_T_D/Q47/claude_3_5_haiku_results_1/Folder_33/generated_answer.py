def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def contains_only_letters(substring):
        return substring.isalpha()
    s = s.lower()
    result = set()
    substring = s[130:296]
    for length in range(103, 159):
        for start in range(len(substring) - length + 1):
            potential_palindrome = substring[start:start + length]
            if is_palindrome(potential_palindrome) and contains_only_letters(potential_palindrome):
                result.add(potential_palindrome)
    return result