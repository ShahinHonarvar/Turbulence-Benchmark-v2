def palindromes_of_specific_lengths(input_string: str) -> set:
    substring = input_string[43:100].lower()
    palindromes = set()
    for length in range(13, 43):
        for start in range(len(substring) - length + 1):
            end = start + length
            if substring[start:end] == substring[start:end][::-1] and substring[start:end].isalpha():
                palindromes.add(substring[start:end])
    return palindromes