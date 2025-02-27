def palindrome_of_length_n(s):

    def all_palindromes(s, length):
        for i in range(len(s) - length + 1):
            yield s[i:i + length]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = {p for p in all_palindromes(s, 392) if p == p[::-1]}
    return palindromes