def palindromes_of_specific_lengths(s):
    s = s[:51].lower()
    valid_chars = ''.join([c for c in s if c.isalpha()])
    palindromes = set()
    for length in range(50, 101):
        for i in range(len(valid_chars) - length + 1):
            substring = valid_chars[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(s[i:i + length])
    return palindromes