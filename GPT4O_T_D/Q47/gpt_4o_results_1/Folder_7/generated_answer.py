def palindromes_of_specific_lengths(s):
    s = s[119:257]
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    palindrome_set = set()
    for length in range(104, 124):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if substr == substr[::-1]:
                palindrome_set.add(substr)
    return palindrome_set