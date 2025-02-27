def palindromes_of_specific_lengths(input_string: str) -> set:
    input_string = input_string.lower()
    palindromes = set()
    substring = input_string[17:66]
    for length in range(23, 37):
        for i in range(len(substring) - length + 1):
            sub_substring = substring[i:i + length]
            if sub_substring == sub_substring[::-1] and sub_substring.isalpha():
                palindromes.add(sub_substring)
    return palindromes