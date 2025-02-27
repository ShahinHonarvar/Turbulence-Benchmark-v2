def palindromes_of_specific_lengths(input_string):
    valid_palindromes = set()
    for length in range(31, 52):
        for index in range(18, 99 - length + 1):
            substring = input_string[index:index + length].lower()
            if substring.isalpha() and substring == substring[::-1]:
                valid_palindromes.add(substring)
    return valid_palindromes