def palindromes_of_specific_lengths(input_string):
    allowed_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(10, 37):
        for start_index in range(24, 98):
            end_index = start_index + length - 1
            if end_index < 100:
                substring = input_string[start_index:end_index + 1]
                if set(substring) <= allowed_characters:
                    if substring == substring[::-1]:
                        palindromes.add(substring.lower())
    return palindromes