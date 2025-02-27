def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 2):
        if s[i] in 'abcdefghijklmnopqrstuvwxyz' and s[i + 1] in 'abcdefghijklmnopqrstuvwxyz' and (s[i + 2] in 'abcdefghijklmnopqrstuvwxyz'):
            substring = s[i:i + 3]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes