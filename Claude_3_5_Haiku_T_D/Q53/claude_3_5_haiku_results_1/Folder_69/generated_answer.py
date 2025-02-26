def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    for start in range(length):
        for end in range(start + 98, length + 1):
            substr = s[start:end]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes