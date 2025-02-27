def palindrome_of_length_n(s):
    palindromes = set()
    s = ''.join((c for c in s if c.isalpha())).lower()
    length = len(s)
    target_length = 131
    for i in range(length - target_length + 1):
        substring = s[i:i + target_length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes