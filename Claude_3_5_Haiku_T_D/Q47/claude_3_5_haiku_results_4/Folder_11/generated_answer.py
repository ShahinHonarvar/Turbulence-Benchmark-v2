def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1] and substring.isalpha()
    s = s.lower()
    substring = s[24:98]
    palindromes = set()
    for length in range(10, 37):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes