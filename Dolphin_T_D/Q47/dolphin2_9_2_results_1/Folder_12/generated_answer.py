def palindromes_of_specific_lengths(s):
    subset = s[62:89]
    lengths = range(18, 22)

    def is_palindrome(s):
        return s == s[::-1]

    def is_english_letter(c):
        return c.isalpha()
    palindromes = set()
    for length in lengths:
        for i in range(len(subset) - length + 1):
            substring = subset[i:i + length]
            if is_palindrome(substring) and all((is_english_letter(c) for c in substring.lower())):
                palindromes.add(substring)
    return palindromes