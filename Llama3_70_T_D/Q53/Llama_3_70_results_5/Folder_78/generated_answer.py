def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    s = s.lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 96, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes