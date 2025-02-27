def palindrome_of_length_n(s):
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    length = len(s)
    for i in range(length - 205):
        substring = s[i:i + 206]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes