def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    for i in range(len(s) - 50):
        if s[i:i + 51] == s[i:i + 51][::-1]:
            palindromes.add(s[i:i + 51])
    return palindromes