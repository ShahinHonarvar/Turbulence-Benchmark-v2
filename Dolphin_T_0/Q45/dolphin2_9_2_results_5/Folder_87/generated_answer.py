def palindromes_between_indices(string):
    string = string[3:9].lower()
    for char in '!@#$%^&*()':
        string = string.replace(char, '')
    palindromes = set()
    for i in range(len(string)):
        if len(string) - i < 3:
            break
        for j in range(i + 3, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes