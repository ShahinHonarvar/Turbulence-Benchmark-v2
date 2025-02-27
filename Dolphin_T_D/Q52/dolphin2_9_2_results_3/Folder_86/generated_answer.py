def palindrome_of_length_n(s):
    s = ''.join((c for c in s if c.isalpha()))
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 181 + 1):
        if s[i:i + 181] == s[i:i + 181][::-1]:
            palindromes.add(s[i:i + 181])
    return palindromes