def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    input_string = input_string.lower()
    for i in range(1, 9):
        for j in range(len(input_string) - i):
            if i >= 3 and i <= 4:
                substring = input_string[j:j + i]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes