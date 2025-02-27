def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    length = len(s)
    for i in range(length - 91):
        substring = s[i:i + 92]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes