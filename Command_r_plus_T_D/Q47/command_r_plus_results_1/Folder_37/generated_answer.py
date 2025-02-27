def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[:10].lower()
    for length in range(3, 6):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1]:
                palindromes.add(substring[i:i + length])
    return palindromes