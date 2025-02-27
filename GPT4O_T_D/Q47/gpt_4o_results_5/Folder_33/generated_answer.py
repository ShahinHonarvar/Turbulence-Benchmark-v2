def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    filtered = ''.join([c.lower() for c in s[130:296] if c.isalpha()])
    palindromes = set()
    for length in range(103, 159):
        for i in range(len(filtered) - length + 1):
            substring = filtered[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes