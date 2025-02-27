def palindromes_of_specific_lengths(input_string):
    input_string = input_string[22:96]
    palindromes = set()
    for length in range(52, 56):
        for i in range(len(input_string) - length + 1):
            sub_string = input_string[i:i + length]
            if set(sub_string.lower()) <= set('abcdefghijklmnopqrstuvwxyz') and sub_string.lower() == sub_string.lower()[::-1]:
                palindromes.add(sub_string)
    return palindromes