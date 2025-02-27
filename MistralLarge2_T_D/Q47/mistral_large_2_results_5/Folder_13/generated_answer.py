def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[13:96]
    lower_substring = substring.lower()
    palindromes = set()
    for length in range(57, 61):
        for i in range(len(lower_substring) - length + 1):
            sub = lower_substring[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(substring[i:i + length])
    return palindromes