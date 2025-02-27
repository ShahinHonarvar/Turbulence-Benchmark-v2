def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    length = len(s)
    palindromes = set()
    for i in range(length - 36):
        substring = s[i:i + 37]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes