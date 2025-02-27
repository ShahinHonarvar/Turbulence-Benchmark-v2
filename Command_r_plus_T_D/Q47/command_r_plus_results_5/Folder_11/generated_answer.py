def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[23:98].lower()
    for length in range(10, 37):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes