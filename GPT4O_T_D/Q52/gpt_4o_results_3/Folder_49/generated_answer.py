def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 47
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(s[i:i + n])
    return palindromes