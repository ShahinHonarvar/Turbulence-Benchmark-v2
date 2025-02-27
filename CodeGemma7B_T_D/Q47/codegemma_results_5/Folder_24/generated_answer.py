def palindromes_of_specific_lengths(input_string):
    lowercase_string = input_string.lower()
    palindromes = set()
    for i in range(12, 93):
        for j in range(42, 78):
            substring = lowercase_string[i - j:i + j + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes