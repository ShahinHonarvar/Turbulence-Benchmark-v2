def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    if length < 93:
        return palindromes
    for i in range(length - 92):
        for j in range(i + 93, length + 1):
            substr = s[i:j]
            if len(substr) == 93 and substr.isalpha() and (substr == substr[::-1]):
                palindromes.add(substr)
    return palindromes