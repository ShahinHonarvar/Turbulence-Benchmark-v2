def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    for i in range(1, 8):
        for j in range(i, len(input_string), i):
            if input_string[j:j + i].lower() == input_string[j + i - 1:j - 1:-1].lower() and input_string[j:j + i].isalpha() and (3 <= i <= 4):
                palindromes.add(input_string[j:j + i])
    return palindromes