def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    for i in range(36, 93):
        for j in range(10, 36):
            if i + j - 1 <= 92:
                substring = input_string[i:i + j].lower()
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes