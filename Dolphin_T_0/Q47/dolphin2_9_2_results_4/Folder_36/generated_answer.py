def palindromes_of_specific_lengths(string):
    string = string[124:284]
    palindromes = set()
    for i in range(115, 135):
        for j in range(len(string) - i + 1):
            substring = string[j:j + i]
            if substring == substring[::-1] and all((x.isalpha() for x in substring)):
                palindromes.add(substring.lower())
    return palindromes