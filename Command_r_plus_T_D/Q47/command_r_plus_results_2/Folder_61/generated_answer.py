def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    input_string = input_string[:31].lower()
    for length in range(20, 31):
        for start in range(len(input_string) - length + 1):
            substring = input_string[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes