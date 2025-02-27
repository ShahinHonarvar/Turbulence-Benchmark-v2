def palindrome_of_length_n(input_string):
    palindromes = set()
    for i in range(len(input_string) - 65):
        sub_string = input_string[i:i + 66]
        lower_case_substring = sub_string.lower()
        if lower_case_substring == lower_case_substring[::-1]:
            palindromes.add(sub_string)
    return palindromes