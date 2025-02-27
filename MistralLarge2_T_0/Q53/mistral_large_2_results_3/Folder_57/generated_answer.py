def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 93, length + 1):
            sub = s[i:j]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes