def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    for length in range(18, 48):
        for index in range(43, 96 - length):
            if input_string[index:index + length].lower() == input_string[index:index + length][::-1].lower():
                palindromes.add(input_string[index:index + length])
    return palindromes