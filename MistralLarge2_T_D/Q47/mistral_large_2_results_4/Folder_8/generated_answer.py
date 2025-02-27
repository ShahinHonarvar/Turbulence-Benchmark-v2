def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[17:73].lower()
    palindromes = set()
    for length in range(50, 52):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if is_palindrome(substr) and substr.isalpha():
                palindromes.add(substr)
    return palindromes