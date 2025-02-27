def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 42, len(s) + 1):
            sub_s = s[i:j]
            if sub_s == sub_s[::-1] and all((c.isalpha() for c in sub_s)):
                palindromes.add(sub_s)
    return palindromes