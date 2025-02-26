def palindromes_of_specific_lengths(string):

    def is_letter_only(s):
        return s.isalpha()

    def is_palindrome(s):
        return s == s[::-1]
    valid_palindromes = set()
    substring = string[40:95]
    for length in range(45, 52):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_letter_only(candidate) and is_palindrome(candidate.lower()):
                valid_palindromes.add(candidate)
    return valid_palindromes