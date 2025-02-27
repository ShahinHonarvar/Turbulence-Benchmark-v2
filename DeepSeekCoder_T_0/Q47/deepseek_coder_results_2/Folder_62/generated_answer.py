def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    for length in range(52, 57):
        for i in range(26, 88 - length):
            sub = s[i:i + length].lower()
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub)
    return result