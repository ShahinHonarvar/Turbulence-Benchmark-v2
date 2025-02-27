def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower() and sub.isalpha()
    palindromes = set()
    for length in range(7, len(s) + 1):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes