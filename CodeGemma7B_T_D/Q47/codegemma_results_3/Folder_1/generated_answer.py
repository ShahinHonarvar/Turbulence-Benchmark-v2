def palindromes_of_specific_lengths(string):
    palindromes = set()
    string = string.lower()
    for i in range(15, 89):
        for j in range(i + 40, i + 73):
            if string[i:j] == string[j - 1:i - 1:-1]:
                palindromes.add(string[i:j])
    return palindromes