def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_letter_only(word):
        return word.isalpha()
    palindromes = set()
    s = s.lower()
    for length in range(90, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring) and is_letter_only(substring):
                palindromes.add(substring)
    return palindromes