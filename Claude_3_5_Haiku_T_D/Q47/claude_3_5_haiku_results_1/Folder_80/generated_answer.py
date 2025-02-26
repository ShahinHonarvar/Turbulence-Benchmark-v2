def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]

    def is_alpha(word):
        return word.isalpha()
    substring = s[35:89]
    palindromes = set()
    for length in range(24, 34):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate) and is_alpha(candidate):
                palindromes.add(candidate.lower())
    return palindromes