def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            sub_s = s[i:j]
            if sub_s == sub_s[::-1] and len(sub_s) == 3:
                palindromes.add(sub_s)
    return palindromes