def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    result = set()
    for length in range(3, 8):
        for i in range(1, 10):
            if i + length <= 10:
                sub = s[i:i + length]
                if sub.isalpha() and is_palindrome(sub):
                    result.add(sub.lower())
    return result