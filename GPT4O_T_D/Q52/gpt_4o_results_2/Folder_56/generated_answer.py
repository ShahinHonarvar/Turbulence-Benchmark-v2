def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    length = len(s)
    for i in range(length - 94):
        substring = s[i:i + 95]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes