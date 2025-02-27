def palindrome_of_length_n(s):
    s = ''.join((e for e in s if e.isalpha())).lower()
    n = 6
    palindromes = set()
    for i in range(len(s) - n + 1):
        if s[i:i + n] == s[i:i + n][::-1]:
            palindromes.add(s[i:i + n])
    return palindromes