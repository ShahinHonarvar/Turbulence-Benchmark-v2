def palindromes_of_specific_lengths(string):
    string = string[12:100]
    palindromes = set()
    for i in range(26, 30):
        for j in range(len(string) - i + 1):
            substring = string[j:j + i]
            if all((char.isalpha() for char in substring)):
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes