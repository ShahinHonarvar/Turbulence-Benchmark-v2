def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    input_string = input_string[15:95]
    for length in range(20, 67):
        for i in range(len(input_string) - length + 1):
            sub_string = input_string[i:i + length]
            if sub_string.lower() == sub_string.lower()[::-1] and sub_string.isalpha():
                palindromes.add(sub_string)
    return palindromes