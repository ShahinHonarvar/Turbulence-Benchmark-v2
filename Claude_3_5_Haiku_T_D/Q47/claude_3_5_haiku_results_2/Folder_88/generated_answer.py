def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]

    def is_only_letters(s):
        return s.isalpha()
    palindromes = set()
    substring = text[11:88]
    substring = substring.lower()
    for length in range(4, 6):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_only_letters(candidate):
                palindromes.add(candidate)
    return palindromes