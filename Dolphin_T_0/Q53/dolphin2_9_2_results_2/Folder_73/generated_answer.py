def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(94, len(s) + 1):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1] and s[j:j + i] not in palindromes:
                palindromes.add(s[j:j + i])
    return palindromes