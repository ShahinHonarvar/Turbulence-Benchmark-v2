def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(200, 301):
        for j in range(i + 10, min(i + 51, 301)):
            sub = s[i:j]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes