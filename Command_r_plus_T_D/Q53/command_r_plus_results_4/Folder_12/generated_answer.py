def palindrome_of_length_at_least_n(s):
    s = s.lower()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(s)):
        if s[i] in alphabet:
            for j in range(i + 51, len(s) + 1):
                if j == len(s) or s[j] not in alphabet:
                    substring = s[i:j]
                    if substring == substring[::-1]:
                        palindromes.add(substring)
                    break
    return palindromes