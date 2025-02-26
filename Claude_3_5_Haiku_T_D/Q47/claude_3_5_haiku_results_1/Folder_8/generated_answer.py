def palindromes_of_specific_lengths(s):

    def is_letter_palindrome(substr):
        return substr.isalpha() and substr == substr[::-1]

    def is_valid_length(length):
        return 50 <= length <= 51
    palindromes = set()
    substring = s[17:73].lower()
    for start in range(len(substring)):
        for length in range(50, 52):
            if start + length > len(substring):
                break
            substr = substring[start:start + length]
            if is_letter_palindrome(substr):
                palindromes.add(substr)
    return palindromes