def palindrome_of_length_n(string, length=33):
    palindromes = set()
    string = ''.join((e for e in string if e.isalpha())).lower()
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes