def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def is_alpha(substring):
        return all((char.isalpha() for char in substring))
    palindromes = set()
    substring = s[17:73].lower()
    for length in range(50, 52):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate) and is_alpha(candidate):
                palindromes.add(candidate)
    return palindromes