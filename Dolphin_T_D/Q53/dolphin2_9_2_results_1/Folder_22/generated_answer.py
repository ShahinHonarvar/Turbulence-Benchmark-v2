def palindrome_of_length_at_least_n(s):
    s_lower = s.lower()
    n = 97
    palindromes = set()
    for i in range(len(s_lower)):
        for j in range(i + n, len(s_lower) + 1):
            sub_s = s_lower[i:j]
            if sub_s == sub_s[::-1]:
                palindromes.add(s[i:j])
    return palindromes