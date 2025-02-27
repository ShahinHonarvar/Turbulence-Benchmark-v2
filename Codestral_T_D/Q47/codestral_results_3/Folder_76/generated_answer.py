def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[101:293].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 154, min(i + 183, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes