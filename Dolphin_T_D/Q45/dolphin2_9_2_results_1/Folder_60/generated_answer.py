def palindromes_between_indices(s):
    string = s[3:7]
    string = ''.join(filter(str.isalpha, string))
    string = string.lower()
    string_set = set(string)
    palindromes = set()
    for i in range(4, len(string) + 1):
        for substring in combinations(string, i):
            substring = ''.join(substring)
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes