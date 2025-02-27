def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    for length in range(52, 57):
        for i in range(26, 87 - length + 2):
            sub = s[i:i + length]
            if sub.isalpha() and is_palindrome(sub.lower()):
                result.add(sub.lower())
    return result