def palindrome_of_length_n(s):
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s) - 28):
        substring = s[i:i + 29]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes