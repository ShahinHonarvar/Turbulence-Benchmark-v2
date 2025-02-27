def palindromes_of_specific_lengths(string):
    string = string[16:96].lower()
    length = len(string)
    palindromes = set()
    for i in range(length - 12):
        for j in range(i + 13, min(length, i + 50)):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes