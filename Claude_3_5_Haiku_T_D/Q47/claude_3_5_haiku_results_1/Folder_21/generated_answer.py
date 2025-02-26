def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_letters_only(substring):
        return substring.isalpha()
    palindromes = set()
    if len(s) < 296:
        return palindromes
    substring = s[100:296]
    for length in range(136, 161):
        for start in range(len(substring) - length + 1):
            potential_palindrome = substring[start:start + length]
            if is_palindrome(potential_palindrome) and is_letters_only(potential_palindrome):
                palindromes.add(potential_palindrome)
    return palindromes