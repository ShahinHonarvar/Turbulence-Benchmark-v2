def palindromes_of_specific_lengths(input_string):
    string_section = input_string[26:85]
    palindromes_set = set()
    for length in range(30, 47):
        for i in range(len(string_section) - length + 1):
            substring = string_section[i:length + i]
            lower_substring = substring.lower()
            if lower_substring == lower_substring[::-1] and lower_substring.isalpha():
                palindromes_set.add(substring)
    return palindromes_set