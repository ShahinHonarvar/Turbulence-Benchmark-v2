def palindrome_of_length_n(s):
    target_length = 474
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s) - target_length + 1):
        substring = s[i:i + target_length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes