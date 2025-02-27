def palindromes_of_specific_lengths(s):
    s = s[26:85].lower()

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    for length in range(30, 47):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes