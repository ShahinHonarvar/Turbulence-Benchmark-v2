def palindrome_of_length_n(s):
    palindromes = set()
    clean_s = ''.join(filter(str.isalpha, s.lower()))
    length = 318
    if len(clean_s) < length:
        return palindromes
    for i in range(len(clean_s) - length + 1):
        substring = clean_s[i:i + length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes