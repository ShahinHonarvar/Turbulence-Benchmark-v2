def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    palindromes = set()
    for length in range(154, 183):
        for start in range(101, 293 - length):
            substring = s[start:start + length]
            filtered = ''.join([c for c in substring if c.isalpha()])
            if len(filtered) == length and is_palindrome(filtered):
                palindromes.add(filtered)
    return palindromes