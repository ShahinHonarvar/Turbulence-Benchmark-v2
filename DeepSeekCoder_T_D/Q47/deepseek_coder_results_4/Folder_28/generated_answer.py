def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    result = set()
    for length in range(21, 33):
        for i in range(32, 72 - length):
            sub = s[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub.lower())
    return result