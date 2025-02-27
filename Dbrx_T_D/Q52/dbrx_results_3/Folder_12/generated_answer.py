def palindrome_of_length_n(s):
    palindromes = set()
    s = ''.join((e for e in s if e.isalpha())).lower()
    if len(s) < 23:
        return palindromes
    for i in range(len(s) - 23 + 1):
        if s[i:i + 23] == s[i:i + 23][::-1]:
            palindromes.add(s[i:i + 23])
    return palindromes