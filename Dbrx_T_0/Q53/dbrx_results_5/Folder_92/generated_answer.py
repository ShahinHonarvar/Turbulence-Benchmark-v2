def palindrome_of_length_at_least_n(s):
    s = ''.join((e for e in s if e.isalpha())).lower()
    palindromes = set()
    for i in range(len(s) - 9):
        for j in range(i + 5, len(s) - i + 1, 2):
            if s[i:j] == s[i:j][::-1] and s[i:j] not in palindromes:
                palindromes.add(s[i:j])
    return palindromes