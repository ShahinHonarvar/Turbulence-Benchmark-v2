def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 16):
        for j in range(i + 17, len(string) + 1):
            substring = string[i:j]
            if len(set(substring)) == 1:
                continue
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes