def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.replace('.', '').replace(',', '').replace('?', '').replace('!', '')
    n = len(s)
    s = s.lower()
    for i in range(n):
        for j in range(i + 137, n):
            sub_s = s[i:j + 1]
            if sub_s == sub_s[::-1]:
                palindromes.add(sub_s)
    return palindromes