def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[:11].lower()
    for length in range(3, 6):
        for start in range(0, len(substring) - length + 1):
            end = start + length
            temp_substring = substring[start:end]
            if temp_substring == temp_substring[::-1] and temp_substring.isalpha():
                palindromes.add(temp_substring)
    return palindromes