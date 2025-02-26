def palindromes_of_specific_lengths(string):

    def is_palindrome(s):
        return s == s[::-1]

    def is_letters_only(s):
        return s.isalpha()
    palindromes = set()
    substring = string[18:88]
    for length in range(38, 61):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length].lower()
            if is_palindrome(candidate) and is_letters_only(candidate):
                palindromes.add(candidate)
    return palindromes