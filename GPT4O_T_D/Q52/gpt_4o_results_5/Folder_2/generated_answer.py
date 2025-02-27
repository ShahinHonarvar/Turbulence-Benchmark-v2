def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    palindromes = set()
    length = len(s)
    target_length = 147
    for i in range(length - target_length + 1):
        substring = s[i:i + target_length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes