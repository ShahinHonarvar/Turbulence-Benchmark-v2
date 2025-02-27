def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for length in range(27, n + 1):
        for i in range(n - length + 1):
            sub_str = s[i:i + length]
            if sub_str == sub_str[::-1] and sub_str.isalpha():
                palindromes.add(sub_str)
    return palindromes