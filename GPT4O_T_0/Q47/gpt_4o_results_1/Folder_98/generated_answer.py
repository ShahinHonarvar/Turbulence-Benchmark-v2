def palindromes_of_specific_lengths(s):
    s = s[:21]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 5, min(n, i + 81)):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes