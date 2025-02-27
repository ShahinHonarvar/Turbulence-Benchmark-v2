def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    n = len(s)
    palindromes = set()
    for length in range(10, 51):
        for i in range(200, 301 - length):
            sub = s[i:i + length]
            if is_palindrome(sub.lower()) and sub.isalpha():
                palindromes.add(sub)
    return palindromes