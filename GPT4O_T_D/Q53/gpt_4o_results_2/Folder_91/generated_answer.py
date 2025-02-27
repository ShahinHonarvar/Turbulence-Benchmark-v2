def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    length = len(s)
    for start in range(length):
        for end in range(start + 7, length + 1):
            substr = s[start:end]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes