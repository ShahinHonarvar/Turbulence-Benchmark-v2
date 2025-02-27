def palindromes_of_specific_lengths(s):
    s = s[29:99].lower()
    palindromes_set = set()
    for length in range(6, 10):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes_set.add(substring)
    return palindromes_set