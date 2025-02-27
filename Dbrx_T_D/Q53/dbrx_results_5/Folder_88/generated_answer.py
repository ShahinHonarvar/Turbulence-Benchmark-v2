def palindrome_of_length_at_least_n(s):
    s = ''.join((e for e in s if e.isalpha())).lower()
    palindromes = set()
    for i in range(len(s) - 26):
        for j in range(i, i + 27):
            if s[i:j + 1] == s[i:j + 1][::-1] and s[i:j + 1] not in palindromes:
                palindromes.add(s[i:j + 1])
    return palindromes