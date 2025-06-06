def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(s) - 68):
        substring = s[i:i + 69]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes