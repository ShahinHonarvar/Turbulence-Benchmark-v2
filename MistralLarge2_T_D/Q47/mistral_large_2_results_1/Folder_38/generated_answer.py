def palindromes_of_specific_lengths(s):

    def is_palindrome(subs):
        return subs.lower() == subs.lower()[::-1]
    result = set()
    for length in range(38, 61):
        for start in range(18, 87 - length + 2):
            end = start + length - 1
            substring = s[start:end + 1]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring)
    return result