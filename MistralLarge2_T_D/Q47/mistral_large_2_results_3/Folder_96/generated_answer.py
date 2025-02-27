def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def find_palindromes(start, end):
        palindromes = set()
        for length in range(50, 101):
            for i in range(start, end - length + 1):
                substring = s[i:i + length]
                if substring.isalpha() and is_palindrome(substring.lower()):
                    palindromes.add(substring)
        return palindromes
    return find_palindromes(100, 301)