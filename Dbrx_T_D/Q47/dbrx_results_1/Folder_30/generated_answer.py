def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    for length in range(55, 72):
        for start in range(14, len(input_string) - length + 1):
            substring = input_string[start:start + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes