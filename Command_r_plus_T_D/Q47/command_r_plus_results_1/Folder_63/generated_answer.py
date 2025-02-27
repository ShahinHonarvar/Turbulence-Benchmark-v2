def palindromes_of_specific_lengths(input_string: str) -> set:
    substring = input_string[33:86]
    palindromes = set()
    for length in range(26, 32):
        for i in range(len(substring) - length + 1):
            current_substring = substring[i:i + length]
            if current_substring.lower() == current_substring[::-1].lower():
                palindromes.add(current_substring)
    return palindromes