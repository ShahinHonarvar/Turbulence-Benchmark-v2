def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]

    def get_palindromes(s):
        length = len(s)
        palindromes = set()
        for i in range(length):
            for j in range(i + 1, length + 1):
                substring = s[i:j]
                if is_palindrome(substring):
                    palindromes.add(substring.lower())
        return palindromes
    return get_palindromes(s)