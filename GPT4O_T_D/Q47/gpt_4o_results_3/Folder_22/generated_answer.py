def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = s.lower()
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    substr = ''.join([c for c in s[100:201] if c in valid_chars])
    result = set()
    for length in range(5, 11):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if is_palindrome(candidate):
                result.add(candidate)
    return result