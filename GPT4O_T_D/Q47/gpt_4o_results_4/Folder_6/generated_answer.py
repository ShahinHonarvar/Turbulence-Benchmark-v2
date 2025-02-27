def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[45:99].lower()
    result = set()
    for start in range(len(s)):
        for length in range(40, 48):
            end = start + length
            if end > len(s):
                continue
            substring = s[start:end]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring)
    return result