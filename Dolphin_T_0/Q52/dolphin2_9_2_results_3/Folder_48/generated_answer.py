def palindrome_of_length_n(s):
    n = 186
    letters = 'abcdefghijklmnopqrstuvwxyz'
    s = ''.join((e for e in s if e.isalpha())).lower()
    if len(set(s)) < n:
        return set()
    palindromes = set()
    for i in range(len(s) - n + 1):
        if all((s[i + j] == s[i + j + n - 1] for j in range(n // 2))):
            palindromes.add(s[i:i + n])
    return palindromes