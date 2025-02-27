def palindromes_of_specific_lengths(s):

    def is_palindrome(candidate):
        return candidate == candidate[::-1]
    filtered_s = ''.join((c for c in s if c.isalpha())).lower()
    result = set()
    for length in range(50, 101):
        for i in range(100, 301 - length + 1):
            candidate = filtered_s[i:i + length]
            if is_palindrome(candidate):
                result.add(s[i:i + length])
    return result