def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(s) - 82):
        substring = s[i:i + 83]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes