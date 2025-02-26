def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def contains_only_letters(substring):
        return substring.isalpha()
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 98):
        substring = s[i:i + 99]
        if len(substring) == 99 and is_palindrome(substring) and contains_only_letters(substring):
            palindromes.add(substring)
    return palindromes