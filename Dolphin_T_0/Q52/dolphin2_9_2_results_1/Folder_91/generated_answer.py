def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 6):
        if s[i] in 'abcdefghijklmnopqrstuvwxyz':
            for j in range(i + 3, len(s) - 3):
                if s[j] in 'abcdefghijklmnopqrstuvwxyz':
                    if s[i:j + 1][::-1] == s[i:j + 1]:
                        palindromes.add(s[i:j + 1])
    return palindromes