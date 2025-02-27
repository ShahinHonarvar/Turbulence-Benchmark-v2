def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    length = 423
    palindromes = set()
    for i in range(len(s) - length + 1):
        substr = s[i:i + length]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes