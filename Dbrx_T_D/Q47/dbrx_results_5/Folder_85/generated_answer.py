def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    for i in range(29, 99):
        for j in range(6, 10):
            substring = input_string[i:i + j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes