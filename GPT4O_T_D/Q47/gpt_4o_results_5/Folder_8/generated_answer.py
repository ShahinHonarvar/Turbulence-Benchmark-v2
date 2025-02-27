def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = ''.join(filter(str.isalpha, s[17:73]))
    palindromes = set()
    for length in range(50, 52):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring.lower())
    return palindromes