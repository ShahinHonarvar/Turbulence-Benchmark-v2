def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    substr = s[41:90]
    length = len(substr)
    for i in range(length):
        for j in range(i + 23, min(i + 39, length + 1)):
            sub = substr[i:j]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes