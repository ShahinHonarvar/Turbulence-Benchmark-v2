def palindrome_of_length_n(s):
    s = s.lower()
    len_s = len(s)
    palindromes = set()
    for i in range(len_s - 67):
        for j in range(i + 68, len_s + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes