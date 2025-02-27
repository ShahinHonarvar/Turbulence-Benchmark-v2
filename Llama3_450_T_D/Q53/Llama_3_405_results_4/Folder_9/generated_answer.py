def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    for length in range(95, len(s) + 1):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes