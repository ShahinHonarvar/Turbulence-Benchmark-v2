def palindromes_of_specific_lengths(input_string):
    input_string = input_string[23:83]
    palindromes = set()
    for i in range(len(input_string) - 32):
        for j in [32, 33, 34]:
            if input_string[i:i + j].lower() == input_string[i:i + j][::-1].lower():
                palindromes.add(input_string[i:i + j])
    return palindromes