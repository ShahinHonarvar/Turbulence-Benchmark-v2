def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_alpha_only(word):
        return word.isalpha()
    palindromes = set()
    if len(s) < 63:
        return palindromes
    substring = s[21:63]
    for length in range(22, 34):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length].lower()
            if is_palindrome(candidate) and is_alpha_only(candidate):
                palindromes.add(candidate)
    return palindromes