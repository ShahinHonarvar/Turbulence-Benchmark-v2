def palindromes_of_specific_lengths(input_string):
    target_substring = input_string[155:284].lower()
    palindromes = set()
    for i in range(len(target_substring) - 103):
        for j in range(104, 121):
            substring = target_substring[i:i + j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes