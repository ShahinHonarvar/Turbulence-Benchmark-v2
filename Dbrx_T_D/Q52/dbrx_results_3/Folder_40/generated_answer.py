def palindrome_of_length_n(string):
    palindromes = set()
    string = ''.join((c.lower() for c in string if c.isalpha()))
    for i in range(len(string) - 2):
        for j in range(i + 1, len(string) - 1):
            if string[i] == string[j + 1]:
                palindromes.add(string[i:j + 2])
    return palindromes