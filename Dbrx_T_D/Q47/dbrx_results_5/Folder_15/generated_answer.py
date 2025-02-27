def palindromes_of_specific_lengths(string):
    palindromes = set()
    string = string.casefold()
    for length in range(3, 7):
        for index in range(len(string) - length + 1):
            if string[index:index + length] == string[index:index + length][::-1]:
                palindromes.add(string[index:index + length])
    return palindromes