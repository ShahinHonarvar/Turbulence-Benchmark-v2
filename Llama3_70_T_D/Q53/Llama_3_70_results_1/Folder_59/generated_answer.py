def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(20, len(s) + 1):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes