def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    length = 13
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes