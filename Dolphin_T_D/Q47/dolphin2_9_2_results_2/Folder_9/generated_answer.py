def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(301):
        for j in range(i + 49, 301):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set