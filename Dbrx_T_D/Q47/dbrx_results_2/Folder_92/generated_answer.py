def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    for start_index in range(0, 5):
        for length in (3, 4):
            if start_index <= len(input_string) - length:
                substring = input_string[start_index:start_index + length].lower()
                if substring[0].isalpha() and substring[~0].isalpha() and all((substring[i] == substring[~i] for i in range(1, len(substring)))):
                    palindromes.add(substring)
    return palindromes