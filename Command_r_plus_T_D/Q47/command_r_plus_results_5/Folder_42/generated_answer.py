def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[42:96].lower()
    for length in range(18, 48):
        for start in range(0, len(substring) - length + 1):
            current_substring = substring[start:start + length]
            if current_substring == current_substring[::-1] and current_substring.isalpha():
                palindromes.add(current_substring)
    return palindromes