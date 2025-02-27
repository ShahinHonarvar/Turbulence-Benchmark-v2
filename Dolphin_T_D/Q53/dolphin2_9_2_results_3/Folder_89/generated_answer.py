def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for length in range(43, len(s) + 1):
        for i in range(len(s) - length + 1):
            chunk = s[i:i + length]
            if chunk == chunk[::-1]:
                palindromes.add(chunk)
    return palindromes