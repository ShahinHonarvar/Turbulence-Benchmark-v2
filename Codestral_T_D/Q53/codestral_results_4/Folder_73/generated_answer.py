def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 94
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            sub_s = s[i:j]
            if sub_s == sub_s[::-1] and sub_s.isalpha():
                palindromes.add(sub_s)
    return palindromes