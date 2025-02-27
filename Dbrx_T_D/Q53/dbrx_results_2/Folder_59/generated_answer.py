def palindrome_of_length_at_least_n(s):
    s = ''.join((e.lower() for e in s if e.isalpha()))
    palindromes = set()
    for i in range(len(s) - 19):
        for j in range(i + 20, len(s) + 1, 20):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes