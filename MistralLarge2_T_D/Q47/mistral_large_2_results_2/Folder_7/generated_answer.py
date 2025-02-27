def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[119:257].lower()
    palindromes = set()
    for length in range(104, 124):
        for start in range(119, 257 - length + 1):
            candidate = substring[start - 119:start - 119 + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes