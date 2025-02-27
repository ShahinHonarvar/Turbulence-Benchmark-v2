def palindrome_of_length_n(string, length):
    palindromes = set()
    string = ''.join((e.lower() for e in string if e.isalpha()))
    if length % 2 == 1:
        center = length // 2
        for i in range(len(string) - center):
            substring = string[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    else:
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes