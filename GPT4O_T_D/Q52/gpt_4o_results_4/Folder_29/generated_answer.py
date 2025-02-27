def palindrome_of_length_n(s):
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s) - 18):
        substring = s[i:i + 19]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes