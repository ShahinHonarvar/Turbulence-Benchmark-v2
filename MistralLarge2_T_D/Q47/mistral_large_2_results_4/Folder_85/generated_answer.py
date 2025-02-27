def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[29:99].lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(6, 10):
            if i + j <= length:
                substring = s[i:i + j]
                if substring.isalpha() and is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes