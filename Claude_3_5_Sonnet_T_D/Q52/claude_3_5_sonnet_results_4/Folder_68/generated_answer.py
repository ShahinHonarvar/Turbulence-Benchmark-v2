def palindrome_of_length_n(s):
    s = ''.join((char.lower() for char in s if char.isalpha()))
    n = 76
    palindromes = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes