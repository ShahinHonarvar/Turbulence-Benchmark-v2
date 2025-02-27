def palindromes_of_specific_lengths(input_string: str) -> set:
    input_string = input_string.lower()
    palindromes = set()
    for length in range(29, 63):
        for start in range(11, 98 - length):
            substring = input_string[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes