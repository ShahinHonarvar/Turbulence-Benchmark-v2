def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    desired_length = 43
    palindromes = set()
    for i in range(n - desired_length + 1):
        substring = s[i:i + desired_length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes