def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    length = len(s)
    for i in range(6):
        for j in range(3, 6):
            if i + j <= length:
                substring = s[i:i + j].lower()
                if substring.isalpha() and is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes