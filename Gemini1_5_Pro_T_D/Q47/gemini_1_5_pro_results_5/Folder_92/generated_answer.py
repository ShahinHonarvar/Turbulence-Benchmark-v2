def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(0, 5):
        for j in range(i + 3, min(i + 5, 6)):
            substring = string[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes