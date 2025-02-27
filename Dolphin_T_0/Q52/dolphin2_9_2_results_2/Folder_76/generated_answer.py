def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 256):
        if s[i:i + 257] == s[i:i + 257][::-1] and s[i:i + 257].isalpha():
            palindromes.add(s[i:i + 257])
    return palindromes