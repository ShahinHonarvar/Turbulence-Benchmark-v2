def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    length = len(s)
    palindromes = set()
    for i in range(length - 19):
        substring = s[i:i + 20]
        if substring == substring[::-1]:
            palindromes.add(''.join((s[j] for j in range(i, i + 20))))
    return palindromes