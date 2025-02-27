def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = ''.join((e for e in s if e.isalnum()))
    palindromes = set()
    for length in range(57, len(s) + 1):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes