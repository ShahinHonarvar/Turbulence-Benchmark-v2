def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 93):
        sub_s = s[i:i + 94]
        if sub_s == sub_s[::-1]:
            palindromes.add(sub_s)
    return palindromes