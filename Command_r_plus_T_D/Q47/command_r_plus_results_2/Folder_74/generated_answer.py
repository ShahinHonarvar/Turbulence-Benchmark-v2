def palindromes_of_specific_lengths(input_string: str) -> set:
    input_string = input_string.lower()
    palindromes = set()
    substring = input_string[30:85]
    for length in range(12, 21):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1] and substring[i:i + length].isalpha():
                palindromes.add(substring[i:i + length])
    return palindromes