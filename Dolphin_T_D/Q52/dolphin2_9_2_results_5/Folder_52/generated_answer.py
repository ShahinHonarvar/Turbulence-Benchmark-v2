def palindrome_of_length_n(s):
    s = s.lower()
    n = 423
    palindromes = set()
    for i in range(len(s) - n + 1):
        if ''.join(reversed(s[i:i + n])) == s[i:i + n]:
            palindromes.add(s[i:i + n])
    return palindromes