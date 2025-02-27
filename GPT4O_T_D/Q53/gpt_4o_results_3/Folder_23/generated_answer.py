def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 18, length):
            substr = s[i:j + 1]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes