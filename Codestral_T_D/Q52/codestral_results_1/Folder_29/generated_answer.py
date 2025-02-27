def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 18):
        sub_s = s[i:i + 19]
        if sub_s == sub_s[::-1] and sub_s.isalpha():
            palindromes.add(sub_s)
    return palindromes