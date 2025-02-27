def palindromes_of_specific_lengths(input_string: str) -> set:
    substring = input_string[100:201]
    palindromes = set()
    for length in range(5, 11):
        for start_index in range(len(substring) - length + 1):
            substring_slice = substring[start_index:start_index + length]
            if substring_slice.isalpha() and substring_slice.lower() == substring_slice[::-1].lower():
                palindromes.add(substring_slice)
    return palindromes