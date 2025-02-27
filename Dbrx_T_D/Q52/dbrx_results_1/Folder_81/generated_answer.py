def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - 98):
        if s[i:i + 99] == s[i:i + 99][::-1]:
            palindromes.add(s[i:i + 99])
    return palindromes