def palindrome_of_length_at_least_n(s):
    s = ''.join((e for e in s if e.isalpha())).lower()
    palindromes = set()
    for i in range(len(s) - 18):
        for j in range(i + 19, len(s) + 1, 2):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes