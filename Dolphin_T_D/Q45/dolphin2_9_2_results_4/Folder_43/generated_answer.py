def palindromes_between_indices(s):
    string = s[2:6]
    string = ''.join(filter(str.isalpha, string))
    string = string.lower()
    if len(set(string)) < 4:
        return set()
    n = len(string)
    palindromes = set()
    for i in range(n):
        for j in range(i + 2, n + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes