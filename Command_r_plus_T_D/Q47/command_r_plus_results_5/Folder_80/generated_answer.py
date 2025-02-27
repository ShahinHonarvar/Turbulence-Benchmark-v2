def palindromes_of_specific_lengths(input_string: str) -> set:
    input_string = input_string.lower()
    substring = input_string[34:89]
    palindromes = set()
    for length in range(24, 34):
        for start in range(len(substring) - length):
            end = start + length
            substring_slice = substring[start:end]
            if substring_slice == substring_slice[::-1] and substring_slice.isalpha():
                palindromes.add(substring_slice)
    return palindromes