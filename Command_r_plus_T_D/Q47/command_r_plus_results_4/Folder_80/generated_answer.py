def palindromes_of_specific_lengths(input_string: str) -> set:
    substring = input_string[34:89].lower()
    palindromes = set()
    for length in range(24, 34):
        for start in range(len(substring) - length):
            end = start + length
            candidate = substring[start:end]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes