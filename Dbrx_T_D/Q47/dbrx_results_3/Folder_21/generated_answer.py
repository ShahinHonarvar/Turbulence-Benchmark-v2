def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    for i in range(100, 296):
        for j in range(136, 161):
            if i + j - 1 <= 295 and i + j - 1 >= 100:
                substring = input_string[i:i + j].lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes