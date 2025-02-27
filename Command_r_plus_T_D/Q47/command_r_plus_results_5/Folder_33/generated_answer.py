def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[129:296].lower()
    for length in range(103, 159):
        for i in range(len(substring) - length + 1):
            current_substring = substring[i:i + length]
            if current_substring == current_substring[::-1] and current_substring.isalpha():
                palindromes.add(current_substring)
    return palindromes