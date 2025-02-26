def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1] and substr.lower().isalpha()
    if len(s) <= 200:
        return set()
    substring = s[100:201]
    palindromes = set()
    for length in range(5, 11):
        for start in range(len(substring) - length + 1):
            substr = substring[start:start + length]
            if is_palindrome(substr):
                palindromes.add(substr.lower())
    return palindromes