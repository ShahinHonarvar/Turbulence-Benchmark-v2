def palindromes_of_specific_lengths(input_str):
    palindromes = set()
    for i in range(35, 89):
        substring = input_str[i:i + 33].lower()
        for length in range(24, 34):
            if len(substring) >= length:
                if substring[:length] == substring[length - 1:][::-1]:
                    palindromes.add(substring[:length])
    return palindromes