def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    palindromes = set()
    for length in range(3, 11):
        for i in range(1, 299 - length + 2):
            sub = s[i:i + length].lower()
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes