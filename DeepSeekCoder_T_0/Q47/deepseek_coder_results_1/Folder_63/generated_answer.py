def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    for length in range(26, 32):
        for i in range(33, 86 - length + 1):
            sub = s[i:i + length].lower()
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub)
    return result