def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for length in range(53, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes