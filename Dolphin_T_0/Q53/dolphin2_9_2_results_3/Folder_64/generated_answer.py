def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 8, len(s)):
            sub_s = s[i:j + 1]
            if set(sub_s) <= set('abcdefghijklmnopqrstuvwxyz') and sub_s == sub_s[::-1]:
                palindromes.add(sub_s)
    return palindromes