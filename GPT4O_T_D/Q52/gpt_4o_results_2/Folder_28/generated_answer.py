def palindrome_of_length_n(s):
    palindromes = set()
    length = 43
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes