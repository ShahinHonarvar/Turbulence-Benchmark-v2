def palindrome_of_length_at_least_n(s):
    palindromes = set()

    def find_palindromes(s, start, end):
        if start > end:
            return
        if end - start >= 94:
            palindrome = s[start:end + 1]
            if palindrome.lower() == palindrome.lower()[::-1]:
                palindromes.add(palindrome)
        find_palindromes(s, start, end - 1)
    for i in range(len(s)):
        find_palindromes(s, i, i)
        find_palindromes(s, i, i + 1)
    return palindromes