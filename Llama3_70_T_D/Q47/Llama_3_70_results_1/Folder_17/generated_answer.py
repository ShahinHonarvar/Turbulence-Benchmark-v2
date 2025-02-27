def palindromes_of_specific_lengths(input_string):
    input_string = input_string[22:96].lower()
    palindromes = set()
    for length in range(52, 56):
        for i in range(len(input_string) - length + 1):
            substring = input_string[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes