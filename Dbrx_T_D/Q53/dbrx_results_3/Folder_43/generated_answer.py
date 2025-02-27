def palindrome_of_length_at_least_n(s):
    s = ''.join((e for e in s if e.isalpha())).lower()
    palindromes = set()
    for i in range(len(s) - 49):
        for j in range(i + 49, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return palindromes