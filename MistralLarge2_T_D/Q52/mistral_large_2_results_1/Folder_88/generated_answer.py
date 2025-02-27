def palindrome_of_length_n(string):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    palindromes = set()
    length = 13
    string_length = len(string)
    for i in range(string_length - length + 1):
        substring = string[i:i + length]
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes