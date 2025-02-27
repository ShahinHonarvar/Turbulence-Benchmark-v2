def palindrome_of_length_n(s):
    s = s.lower()
    length = len(s)
    palindromes = set()

    def is_palindrome(string):
        return string == string[::-1]
    for i in range(length):
        if i + 6 <= length:
            substring = s[i:i + 6]
            if is_palindrome(substring):
                if substring.isalpha():
                    palindromes.add(substring)
    return palindromes