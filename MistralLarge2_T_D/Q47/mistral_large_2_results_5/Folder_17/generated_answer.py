def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    result = set()
    for length in range(52, 56):
        for i in range(22, 96 - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring)
    return result