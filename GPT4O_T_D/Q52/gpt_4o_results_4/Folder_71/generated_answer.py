def palindrome_of_length_n(s):
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    length = len(s)
    n = 78
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes