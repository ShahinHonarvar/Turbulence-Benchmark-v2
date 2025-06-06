def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 55):
        substr = s[i:i + 56]
        if is_palindrome(substr) and substr.isalpha():
            palindromes.add(substr)
    return palindromes