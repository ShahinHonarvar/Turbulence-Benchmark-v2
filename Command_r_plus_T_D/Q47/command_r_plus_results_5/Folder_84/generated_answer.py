def palindromes_of_specific_lengths(input_string: str) -> set:
    input_string = input_string.lower()
    substring = input_string[22:78]
    palindromes = set()
    for length in range(13, 41):
        for i in range(len(substring) - length + 1):
            sub_substring = substring[i:i + length]
            if sub_substring == sub_substring[::-1] and sub_substring.isalpha():
                palindromes.add(sub_substring)
    return palindromes