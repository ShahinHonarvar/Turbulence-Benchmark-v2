def palindrome_of_length_n(s):
    n = 100
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - n + 1):
        if s[i:i + n] == ''.join(reversed(s[i:i + n])):
            if s[i:i + n].isalpha():
                palindromes.add(s[i:i + n])
    return palindromes