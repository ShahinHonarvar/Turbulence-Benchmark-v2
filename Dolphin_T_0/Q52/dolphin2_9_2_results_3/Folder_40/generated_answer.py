def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    length = 3
    palindromes = set()
    for i in range(len(s) - length + 1):
        if s[i:i + length] == s[i:i + length][::-1]:
            palindromes.add(s[i:i + length])
    return palindromes