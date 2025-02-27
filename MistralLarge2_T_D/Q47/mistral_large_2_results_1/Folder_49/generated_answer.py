def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    result = set()
    substring = s[10:101]
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            sub_s = substring[i:i + length]
            if sub_s.isalpha() and is_palindrome(sub_s.lower()):
                result.add(sub_s)
    return result