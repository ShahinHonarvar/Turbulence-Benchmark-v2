def palindrome_of_length_at_least_n(s):
    palindromes = set()
    l = len(s)
    s_lower = s.lower()
    for i in range(l - 37):
        for j in range(i + 2, l + 1):
            if s_lower[i:j].islower() == s_lower[i:j][::-1].islower():
                palindromes.add(s[i:j])
    return palindromes