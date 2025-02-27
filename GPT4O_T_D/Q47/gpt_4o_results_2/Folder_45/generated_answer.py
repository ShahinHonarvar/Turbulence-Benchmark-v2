def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = s[70:141].lower()
    palindromes = set()
    length = len(s)
    for start in range(length):
        for end in range(start + 3, min(start + 61, length + 1)):
            substring = s[start:end]
            if is_palindrome(substring) and substring.isalpha():
                palindromes.add(substring)
    return palindromes