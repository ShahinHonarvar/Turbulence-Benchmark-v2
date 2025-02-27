def palindrome_of_length_n(s):
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    length = len(s)
    for i in range(length - 92):
        substring = s[i:i + 93]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes