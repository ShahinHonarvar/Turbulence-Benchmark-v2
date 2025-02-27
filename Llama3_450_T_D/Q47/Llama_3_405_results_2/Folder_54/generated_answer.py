def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s[27:78]
    palindromes = set()
    for length in range(18, 20):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes