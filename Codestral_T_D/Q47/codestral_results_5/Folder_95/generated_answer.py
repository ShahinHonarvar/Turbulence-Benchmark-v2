def palindromes_of_specific_lengths(string):
    string = string[12:57]
    palindromes = set()
    for length in range(20, 22):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring.lower() == substring.lower()[::-1]:
                if substring.isalpha():
                    palindromes.add(substring)
    return palindromes