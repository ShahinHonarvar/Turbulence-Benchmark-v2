def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        sub = sub.lower()
        return sub == sub[::-1]
    s = s[10:56]
    palindromes = set()
    for i in range(len(s)):
        for j in range(3, 8):
            if i + j <= len(s):
                sub = s[i:i + j]
                if sub.isalpha() and is_palindrome(sub):
                    palindromes.add(sub.lower())
    return palindromes