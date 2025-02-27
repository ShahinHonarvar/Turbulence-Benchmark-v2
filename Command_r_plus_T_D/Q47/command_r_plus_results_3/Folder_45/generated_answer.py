def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[69:140].lower()
    for length in range(3, 61):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1] and substring[i:i + length].isalpha():
                palindromes.add(substring[i:i + length])
    return palindromes