def palindrome_of_length_n(s):
    n = 46
    s = ''.join((e.lower() for e in s if e.isalpha()))
    palindromes = set()
    for i in range(len(s) - n + 1):
        if s[i:i + n] == s[i:i + n][::-1]:
            palindromes.add(s[i:i + n])
    return palindromes