def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = len(s)
    length = 38
    for i in range(n - length + 1):
        sub_str = s[i:i + length]
        if sub_str == sub_str[::-1]:
            palindromes.add(sub_str)
    return palindromes