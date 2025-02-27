def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    result = set()
    s = s[13:100]
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    for length in range(26, 30):
        for i in range(len(s) - length + 1):
            candidate = s[i:i + length]
            if is_palindrome(candidate):
                result.add(candidate)
    return result