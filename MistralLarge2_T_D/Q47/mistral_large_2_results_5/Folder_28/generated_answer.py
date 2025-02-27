def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substr = s[32:72]
    palindromes = set()
    for length in range(21, 33):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if is_palindrome(sub.lower()) and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes