def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    for index in range(1, 8):
        for length in range(3, 5):
            if index + length <= len(input_string):
                substring = input_string[index - 1:index + length - 1].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes