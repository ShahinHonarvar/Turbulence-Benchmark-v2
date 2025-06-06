def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    result = set()
    for length in range(10, 51):
        for i in range(10, 101 - length):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring.lower())
    return result