def palindromes_of_specific_lengths(s):
    string = s[36:93]
    palindromes = set()
    for length in range(10, 36):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring == substring[::-1]:
                if substring.isalpha():
                    palindromes.add(substring.lower())
    return palindromes