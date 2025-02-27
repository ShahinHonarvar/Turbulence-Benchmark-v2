def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 32):
        if s[i:i + 33] == s[i:i + 33][::-1]:
            palindromes.add(s[i:i + 33])
    return palindromes