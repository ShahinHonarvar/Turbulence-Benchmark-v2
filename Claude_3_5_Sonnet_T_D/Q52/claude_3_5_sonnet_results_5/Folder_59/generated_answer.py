def palindrome_of_length_n(s):
    s = ''.join((char.lower() for char in s if char.isalpha()))
    palindromes = set()
    for i in range(len(s) - 38):
        substring = s[i:i + 39]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes