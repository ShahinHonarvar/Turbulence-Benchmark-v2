def palindromes_of_specific_lengths(input_string):
    input_string_lower = input_string.lower()
    sub_string = input_string_lower[1:8]
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(sub_string) - length + 1):
            sub_substring = sub_string[i:i + length]
            if sub_substring == sub_substring[::-1]:
                palindromes.add(sub_substring)
    return palindromes