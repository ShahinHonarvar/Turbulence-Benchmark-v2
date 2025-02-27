def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    palindromes = set()
    length = min(len(s), 10)
    for i in range(length):
        for j in range(3, 6):
            if i + j <= length:
                substring = s[i:i + j].lower()
                if substring.isalpha() and is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes