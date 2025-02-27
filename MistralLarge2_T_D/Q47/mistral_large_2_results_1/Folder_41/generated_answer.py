def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[1:8]
    result = set()
    for i in range(len(s) - 2):
        for length in range(3, 5):
            sub = s[i:i + length]
            if sub.isalpha() and is_palindrome(sub.lower()):
                result.add(sub.lower())
    return result