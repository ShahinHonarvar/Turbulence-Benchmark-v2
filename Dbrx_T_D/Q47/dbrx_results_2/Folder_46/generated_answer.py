def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    for i in range(11, 98):
        for length in range(29, 63):
            substring = input_string[i:i + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes