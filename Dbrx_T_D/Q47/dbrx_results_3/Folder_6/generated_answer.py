def palindromes_of_specific_lengths(input_string):
    input_string = input_string[45:99]
    palindromes = set()
    for length in range(40, 48):
        for i in range(len(input_string) - length + 1):
            if input_string[i:i + length].lower() == input_string[i:i + length][::-1].lower() and input_string[i:i + length].isalpha():
                palindromes.add(input_string[i:i + length])
    return palindromes