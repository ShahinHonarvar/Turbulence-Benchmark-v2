def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    substring = ''.join([c for c in s[100:201] if c in valid_chars])
    n = len(substring)
    palindromes = set()
    for length in range(5, 11):
        for i in range(n - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate):
                palindromes.add(candidate.lower())
    return palindromes