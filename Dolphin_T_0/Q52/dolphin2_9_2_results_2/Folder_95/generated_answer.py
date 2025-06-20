def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 86):
        sub_s = s[i:i + 87]
        if sub_s == sub_s[::-1]:
            palindromes.add(sub_s)
    return palindromes