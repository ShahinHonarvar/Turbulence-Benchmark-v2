def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length - 114):
        for j in range(i + 115, length + 1):
            sub_s = s[i:j]
            if sub_s == sub_s[::-1]:
                palindromes.add(sub_s)
    return palindromes