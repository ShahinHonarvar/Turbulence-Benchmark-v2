import string

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    s = ''.join(filter(lambda x: x in string.ascii_lowercase, s[0:6]))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes