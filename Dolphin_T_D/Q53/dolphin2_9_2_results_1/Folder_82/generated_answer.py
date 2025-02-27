def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 71):
        p = s[i:i + 72]
        if p == p[::-1]:
            palindromes.add(p)
    return palindromes