def palindromes_of_specific_lengths(input_string: str) -> set:
    substring = input_string[32:80].lower()
    palindromes = set()
    for length in range(35, 42):
        for start_index in range(len(substring) - length + 1):
            end_index = start_index + length
            sub_substring = substring[start_index:end_index]
            if sub_substring == sub_substring[::-1] and sub_substring.isalpha():
                palindromes.add(sub_substring)
    return palindromes