def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    valid_palindromes = set()
    substring = s[14:91]
    substring = ''.join(filter(str.isalpha, substring)).lower()
    for length in range(55, 72):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate):
                valid_palindromes.add(candidate)
    return valid_palindromes