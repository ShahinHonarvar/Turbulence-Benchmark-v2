def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        sub = ''.join(filter(str.isalpha, sub)).lower()
        return sub == sub[::-1]
    palindromes = set()
    substring = s[23:95]
    for length in range(17, 56):
        for start in range(0, len(substring) - length + 1):
            sub = substring[start:start + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes