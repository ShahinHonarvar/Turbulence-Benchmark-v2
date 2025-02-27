def palindromes_of_specific_lengths(input_string: str) -> set:
    input_string = input_string.lower()
    palindromes = set()
    substring = input_string[10:60]
    for length in range(18, 37):
        for start in range(len(substring) - length + 1):
            end = start + length
            temp_substring = substring[start:end]
            if temp_substring == temp_substring[::-1] and temp_substring.isalpha():
                palindromes.add(temp_substring)
    return palindromes