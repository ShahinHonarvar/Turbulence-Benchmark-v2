def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[26:88].lower()
    valid_palindromes = set()
    for length in range(52, 57):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if all((c.isalpha() for c in substring)) and is_palindrome(substring):
                valid_palindromes.add(substring)
    return valid_palindromes