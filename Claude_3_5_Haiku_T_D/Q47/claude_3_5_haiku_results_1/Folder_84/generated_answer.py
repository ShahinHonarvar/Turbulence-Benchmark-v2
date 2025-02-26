def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1] and s.isalpha()
    if len(text) < 78:
        return set()
    substring = text[23:78].lower()
    palindromes = set()
    for length in range(13, 41):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes