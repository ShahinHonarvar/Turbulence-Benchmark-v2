def palindrome_of_length_at_least_n(s):
    normalized_str = ''.join((ch.lower() for ch in s if ch.isalpha()))
    n = len(normalized_str)
    palindromes = set()
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = normalized_str[i:j]
            if len(substring) >= 38 and substring == substring[::-1]:
                palindromes.add(s[i:j])
    return palindromes