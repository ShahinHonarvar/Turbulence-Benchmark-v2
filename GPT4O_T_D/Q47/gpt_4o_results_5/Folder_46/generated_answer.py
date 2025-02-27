def palindromes_of_specific_lengths(s):

    def is_palindrome(ss):
        return ss == ss[::-1]
    s = s[11:98]
    filtered = ''.join([c for c in s if c.isalpha()]).lower()
    palindromes = set()
    for length in range(29, 63):
        for i in range(len(filtered) - length + 1):
            substring = filtered[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes