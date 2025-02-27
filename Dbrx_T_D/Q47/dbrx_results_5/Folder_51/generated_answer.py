def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    for i in range(2, 9):
        for j in range(i - 2, i + 1):
            substring = input_string[i:i + j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes