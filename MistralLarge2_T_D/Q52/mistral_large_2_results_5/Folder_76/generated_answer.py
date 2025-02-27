def palindrome_of_length_n(s):
    length = 257
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(s) - length + 1):
        substr = s[i:i + length]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes