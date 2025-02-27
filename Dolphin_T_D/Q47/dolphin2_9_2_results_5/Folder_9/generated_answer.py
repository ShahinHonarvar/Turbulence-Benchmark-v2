def palindromes_of_specific_lengths(string):
    string = string[:300]
    string = string.lower()
    palindromes = set()
    for i in range(50, 61):
        for j in range(0, len(string) - i + 1):
            if string[j:j + i] == string[j:j + i][::-1] and string[j:j + i].isalpha():
                palindromes.add(string[j:j + i])
    return palindromes