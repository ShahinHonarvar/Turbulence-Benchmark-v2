def palindromes_of_specific_lengths(input_string: str) -> set:
    palindromes = set()
    substring = input_string[43:100].lower()
    for length in range(13, 43):
        for start in range(len(substring) - length):
            end = start + length
            sub_sub_string = substring[start:end]
            if sub_sub_string == sub_sub_string[::-1] and sub_sub_string.isalpha():
                palindromes.add(sub_sub_string)
    return palindromes