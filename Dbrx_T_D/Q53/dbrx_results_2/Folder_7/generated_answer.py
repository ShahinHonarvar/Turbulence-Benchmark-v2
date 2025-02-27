def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for center in range(len(s)):
        for length in range(122, len(s) - center + 1):
            if s[center:center + length] == s[center:center + length][::-1]:
                palindromes.add(s[center:center + length])
    return palindromes