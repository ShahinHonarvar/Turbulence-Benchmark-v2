def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1] and s.isalpha()
    substr = s[100:201]
    palindromes = set()
    for length in range(5, 11):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if is_palindrome(sub):
                palindromes.add(sub.lower())
    return palindromes