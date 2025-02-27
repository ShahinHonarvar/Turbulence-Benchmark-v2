def palindrome_of_length_at_least_n(s):
    s = ''.join((e.lower() for e in s if e.isalpha()))
    palindromes = set()
    for i in range(len(s) - 87 + 1):
        for j in range(i + 43, len(s) - i + 1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes