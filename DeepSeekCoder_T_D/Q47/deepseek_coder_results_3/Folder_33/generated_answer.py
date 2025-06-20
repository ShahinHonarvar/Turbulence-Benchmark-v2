def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    result = set()
    for length in range(103, 159):
        for i in range(130, 296 - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub.lower())
    return result