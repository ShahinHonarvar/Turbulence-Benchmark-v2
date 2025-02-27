def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join((c for c in s[11:94] if c.isalpha()))
    s_lower = s.lower()
    palindromes = set()
    for length in range(34, 55):
        for i in range(len(s_lower) - length + 1):
            substring = s_lower[i:i + length]
            if is_palindrome(substring):
                original_substring = s[i:i + length]
                palindromes.add(original_substring)
    return palindromes