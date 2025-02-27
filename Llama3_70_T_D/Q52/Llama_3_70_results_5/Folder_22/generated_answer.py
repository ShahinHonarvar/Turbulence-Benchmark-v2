def palindrome_of_length_n(s):
    s = ''.join((e for e in s if e.isalpha())).lower()
    palindromes = set()
    for i in range(len(s) - 19):
        substring = s[i:i + 20]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes