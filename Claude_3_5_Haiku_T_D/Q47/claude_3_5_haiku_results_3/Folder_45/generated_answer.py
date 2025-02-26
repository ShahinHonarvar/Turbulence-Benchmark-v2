def palindromes_of_specific_lengths(string):

    def is_palindrome(s):
        return s == s[::-1] and s.isalpha()
    substring = string[70:141].lower()
    palindrome_set = set()
    for length in range(3, 61):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate):
                palindrome_set.add(candidate)
    return palindrome_set