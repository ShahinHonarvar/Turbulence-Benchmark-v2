def palindromes_of_specific_lengths(s):

    def is_palindrome(string):
        return string == string[::-1]
    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    substring = s[17:96]
    palindromes = set()
    for length in range(13, 50):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            cleaned = ''.join(filter(lambda c: c in valid_chars, candidate)).lower()
            if len(cleaned) == length and is_palindrome(cleaned):
                palindromes.add(candidate)
    return palindromes