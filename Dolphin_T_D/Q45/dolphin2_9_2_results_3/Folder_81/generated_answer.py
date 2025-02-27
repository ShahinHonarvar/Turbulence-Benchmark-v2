def palindromes_between_indices(string):
    string = ''.join(filter(str.isalpha, string[0:7]))
    if len(string) < 3:
        return set()
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 2, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes