def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]

    def extract_palindromes(s):
        palindromes = set()
        s = s.lower()
        for length in range(77, len(s) + 1):
            for start in range(len(s) - length + 1):
                substring = s[start:start + length]
                if is_palindrome(substring) and substring.isalpha():
                    palindromes.add(substring)
        return palindromes
    return extract_palindromes(text)