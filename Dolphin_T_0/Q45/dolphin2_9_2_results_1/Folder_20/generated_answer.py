def palindromes_between_indices(s):
    sub_s = s[2:9]
    sub_s = ''.join(filter(str.isalpha, sub_s))
    sub_s = sub_s.lower()
    palindromes = set()
    n = len(sub_s)
    for i in range(n):
        for j in range(i + 3, n):
            s = sub_s[i:j + 1]
            if s == s[::-1]:
                palindromes.add(s)
    return palindromes