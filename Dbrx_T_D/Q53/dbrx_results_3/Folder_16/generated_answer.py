def palindrome_of_length_at_least_n(s):
    s = ''.join((e for e in s if e.isalpha())).lower()
    palindromes = set()
    for i in range(len(s) - 118):
        for j in range(119, len(s) - i + 1):
            if s[i:i + j] == s[i:i + j][::-1] and s[i:i + j].isalpha():
                palindromes.add(s[i:i + j])
    return palindromes