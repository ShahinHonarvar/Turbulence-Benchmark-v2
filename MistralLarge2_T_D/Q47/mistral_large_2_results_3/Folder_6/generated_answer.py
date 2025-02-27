def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    specific_range = s[45:99]
    palindromes = set()
    for length in range(40, 48):
        for i in range(len(specific_range) - length + 1):
            sub = specific_range[i:i + length]
            if sub.isalpha() and is_palindrome(sub.lower()):
                palindromes.add(sub)
    return palindromes