def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 60
    palindromes = set()
    for i in range(len(s) - n + 1):
        sub_s = s[i:i + n]
        if sub_s == sub_s[::-1]:
            palindromes.add(sub_s)
    return palindromes