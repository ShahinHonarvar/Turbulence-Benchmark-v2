def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(s) - 41):
        substring = s[i:i + 42]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes