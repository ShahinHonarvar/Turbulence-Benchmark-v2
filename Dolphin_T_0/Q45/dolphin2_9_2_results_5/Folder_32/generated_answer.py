def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[1:8]
    english_letters = set([c for c in substring if c.isalpha()])
    palindromes = set()
    for i in range(5, len(substring) + 1):
        for palindrome in ''.join((c for c in substring if c in english_letters)):
            if is_palindrome(palindrome) and len(palindrome) >= i:
                palindromes.add(palindrome)
    return palindromes