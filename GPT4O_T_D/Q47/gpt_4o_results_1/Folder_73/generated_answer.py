def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    cleaned_s = ''.join((c.lower() for c in s if c.isalpha()))[21:63]
    palindromes = set()
    for size in range(22, 34):
        for i in range(len(cleaned_s) - size + 1):
            substring = cleaned_s[i:i + size]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes