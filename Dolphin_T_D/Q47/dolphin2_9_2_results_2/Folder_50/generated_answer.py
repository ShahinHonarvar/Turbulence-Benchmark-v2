def palindromes_of_specific_lengths(s):
    string = s[35:93]
    string = ''.join((e for e in string if e.isalpha()))
    string = string.lower()
    palindromeSet = set()
    for length in range(10, 36):
        for index in range(len(string) - length + 1):
            substring = string[index:index + length]
            if substring == substring[::-1]:
                palindromeSet.add(substring)
    return palindromeSet