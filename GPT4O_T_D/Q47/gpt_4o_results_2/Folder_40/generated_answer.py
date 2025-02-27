def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    filtered_s = ''.join((c for c in s[:6] if c.isalpha())).lower()
    result = set()
    n = len(filtered_s)
    for length in range(3, 6):
        for i in range(n - length + 1):
            substr = filtered_s[i:i + length]
            if is_palindrome(substr):
                result.add(substr)
    return result