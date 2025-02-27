def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    substring = s[15:95]
    for length in range(18, 74):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate.lower()) and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes