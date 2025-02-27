def palindromes_of_specific_lengths(input_string):
    subset = input_string[27:96]
    palindromes = set()
    for length in range(49, 52):
        for i in range(len(subset) - length + 1):
            substring = subset[i:i + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes