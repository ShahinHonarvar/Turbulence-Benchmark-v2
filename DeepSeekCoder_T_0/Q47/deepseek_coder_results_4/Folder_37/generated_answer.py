def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    for length in range(3, 6):
        for i in range(10):
            if i + length <= 10:
                sub = s[i:i + length].lower()
                if sub.isalpha() and is_palindrome(sub):
                    result.add(sub)
    return result