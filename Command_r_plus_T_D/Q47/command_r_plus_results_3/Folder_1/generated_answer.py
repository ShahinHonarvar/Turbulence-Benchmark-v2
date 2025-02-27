def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[14:90].lower()
    for length in range(40, 73):
        for start_index in range(len(substring) - length + 1):
            end_index = start_index + length
            temp_substring = substring[start_index:end_index]
            if temp_substring == temp_substring[::-1] and temp_substring.isalpha():
                palindromes.add(temp_substring)
    return palindromes