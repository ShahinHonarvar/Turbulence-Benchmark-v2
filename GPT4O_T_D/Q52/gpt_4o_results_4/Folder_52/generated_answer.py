def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    target_length = 423
    for i in range(len(s) - target_length + 1):
        substring = s[i:i + target_length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes