def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    for length in range(30, 301):
        for i in range(3, 301 - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub.lower())
    return palindromes